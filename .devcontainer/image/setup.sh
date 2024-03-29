#!/usr/bin/env bash

REMOTE_USER="${REMOTE_USER:?}"
REMOTE_USER_PASSWD="$(getent passwd "${REMOTE_USER}")"
REMOTE_USER_HOME="$(echo "${REMOTE_USER_PASSWD}" | cut --delimiter ':' --fields 6)"

# Setup default shell
chsh --shell /usr/bin/zsh "${REMOTE_USER}"

# Setup direnv
cat <<EOF >>"${REMOTE_USER_HOME}/.bashrc"
eval "\$(direnv hook bash)"
EOF

cat <<EOF >>"${REMOTE_USER_HOME}/.zshrc"
eval "\$(direnv hook zsh)"
EOF

# Setup starship
cat <<EOF >>"${REMOTE_USER_HOME}/.bashrc"
eval "\$(starship init bash)"
EOF

cat <<EOF >>"${REMOTE_USER_HOME}/.zshrc"
eval "\$(starship init zsh)"
EOF

# Setup secrets directory
mkdir --parents /secrets/

chown --recursive "${REMOTE_USER}:" /secrets/

# Setup shell history cache
mkdir --parents /persist/shellhistory/

touch /persist/shellhistory/.bash_history
touch /persist/shellhistory/.zsh_history

chown --recursive "${REMOTE_USER}:" /persist/shellhistory/

cat <<EOF >>"${REMOTE_USER_HOME}/.bashrc"
export HISTFILE=/persist/shellhistory/.bash_history
EOF

cat <<EOF >>"${REMOTE_USER_HOME}/.zshrc"
export HISTFILE=/persist/shellhistory/.zsh_history
EOF

# Setup trunk cache
mkdir --parents /cache/trunk/

chown --recursive "${REMOTE_USER}:" /cache/trunk/

cat <<EOF >>"${REMOTE_USER_HOME}/.bashrc"
export TRUNK_CACHE=/cache/trunk/
EOF

cat <<EOF >>"${REMOTE_USER_HOME}/.zshrc"
export TRUNK_CACHE=/cache/trunk/
EOF

# Setup poetry cache
mkdir --parents /cache/poetry/

chown --recursive "${REMOTE_USER}:" /cache/poetry/

cat <<EOF >>"${REMOTE_USER_HOME}/.bashrc"
export POETRY_CACHE_DIR=/cache/poetry/
EOF

cat <<EOF >>"${REMOTE_USER_HOME}/.zshrc"
export POETRY_CACHE_DIR=/cache/poetry/
EOF

# Setup npm cache
mkdir --parents /cache/npm/

chown --recursive "${REMOTE_USER}:" /cache/npm/

cat <<EOF >>"${REMOTE_USER_HOME}/.bashrc"
export NPM_CONFIG_CACHE=/cache/npm/
EOF

cat <<EOF >>"${REMOTE_USER_HOME}/.zshrc"
export NPM_CONFIG_CACHE=/cache/npm/
EOF
