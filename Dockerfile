# Use generic base image with Nix installed
FROM nixos/nix:2.16.1 AS env

# Configure Nix
RUN echo "extra-experimental-features = nix-command flakes" >> /etc/nix/nix.conf

# Set working directory to something other than root
WORKDIR /env/

# Copy Nix files
COPY *.nix flake.lock ./

# Build runtime shell closure and activation script
RUN \
    # Mount cached store paths
    --mount=type=cache,target=/nix-store-cache \
    # Mount Nix evaluation cache
    --mount=type=cache,target=/root/.cache/nix \
    # Import cached store if available
    (if [ -f /nix-store-cache/archive.nar ]; then nix-store --import < /nix-store-cache/archive.nar; fi) && \
    # We need to create necessary directories first
    mkdir -p ./build/closure && \
    # Save system to variable so we can reuse it easily
    export _SYSTEM=$(nix eval --impure --raw --expr 'builtins.currentSystem') && \
    # This will build the runtime shell and all its dependencies
    nix build --no-link .#devShells.$_SYSTEM.runtime && \
    # Save all paths needed for runtime shell to a file
    nix path-info --quiet --quiet --quiet --quiet --quiet --recursive .#devShells.$_SYSTEM.runtime > ./build/paths && \
    # Copy all paths to a separate directory
    cp --recursive $(cat ./build/paths) ./build/closure && \
    # Generate activation script for runtime shell and copy it
    nix print-dev-env .#devShells.$_SYSTEM.runtime > ./build/activate && \
    # Save all paths needed for runtime shell to cache
    nix-store --export $(cat ./build/paths) > /nix-store-cache/archive.nar

# Ubuntu is probably the safest choice for a runtime container right now
FROM ubuntu:23.04

# Use bash as default shell
SHELL ["/bin/bash", "-c"]

# Copy runtime shell closure and activation script
COPY --from=env /env/build/closure/ /nix/store/
COPY --from=env /env/build/activate /env/activate

# Set working directory to something other than root
WORKDIR /app/

# Create app user
RUN useradd --create-home app

# Create virtual environment
RUN . /env/activate && python -m venv .venv

# Setup entrypoint for RUN commands
COPY ./scripts/shell.sh ./scripts/shell.sh
SHELL ["./scripts/shell.sh"]

# Copy Poetry files
COPY poetry.lock poetry.toml pyproject.toml ./

# Install dependencies only
RUN \
    # Mount Poetry cache
    --mount=type=cache,target=/root/.cache/pypoetry \
    poetry install --no-interaction --no-root --only main

# Copy source
COPY ./src/ ./src/

# Copy README.md and LICENSE as they are needed for Poetry to work
COPY ./README.md ./LICENSE ./

# Build wheel and install with pip to force non-editable install
# See: https://github.com/python-poetry/poetry/issues/1382
RUN poetry build --no-interaction --format wheel && \
    python -m pip install --no-deps --no-index --no-cache-dir dist/*.whl && \
    rm -rf dist *.egg-info

# Setup main entrypoint
COPY ./scripts/entrypoint.sh ./scripts/entrypoint.sh
ENTRYPOINT ["./scripts/entrypoint.sh", "litestar-example"]
CMD []
