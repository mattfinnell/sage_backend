git config --global user.email "mattfinnell104@gmail.com"
git config --global user.name "Matt Finnell"

ssh-keygen -t ed25519 -C "mattfinnell104@gmail.com" 
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
cat ~/.ssh/id_ed25519.pub > .out/githubkey
echo "New Github Key Emitted | .out/githubkey"