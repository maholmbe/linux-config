# Lines configured by zsh-newuser-install
HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=1000
setopt autocd extendedglob nomatch notify
unsetopt beep
bindkey -e
# End of lines configured by zsh-newuser-install

source ~/.ssh/ssh-agent-env

# Aliases
alias ls='ls -l'
#alias cp='rsync -ah --info=progress2'

# The following lines were added by compinstall
zstyle :compinstall filename '/home/mats/.zshrc'

autoload -Uz compinit
compinit
# End of lines added by compinstall

# Download Znap, if it's not there yet.
[[ -r ~/git-repos/znap/znap.zsh ]] ||
    git clone --depth 1 -- \
        https://github.com/marlonrichert/zsh-snap.git ~/git-repos/znap
source ~/git-repos/znap/znap.zsh  # Start Znap

# `znap source` starts plugins.
znap source zsh-users/zsh-autosuggestions
znap source zdharma-continuum/fast-syntax-highlighting
znap source zsh-users/zsh-history-substring-search

# znap eval zoxide 'zoxide init zsh'
# znap eval fzf 'fzf --zsh'

#znap eval starship 'starship init zsh'
znap prompt

#Plugin configurations

#history-substring-search
bindkey '^[[A' history-substring-search-up
bindkey '^[[B' history-substring-search-down


eval "$(starship init zsh)"
eval "$(zoxide init zsh)"
#eval $(thefuck --alias)
#eval "$(zoxide init zsh)"

# Import colorscheme from 'wal' asynchronously
# &   # Run the process in the background.
# ( ) # Hide shell job control messages.
# Not supported in the "fish" shell.
#(cat ~/.cache/wal/sequences &)
