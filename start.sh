echo "Cloning Repo...."
git clone https://github.com/Hintpirox/blackmen.git /blackmen
cd /blackmen
pip3 install -r requirements.txt
echo "Starting Bot...."
python3 bot.py
