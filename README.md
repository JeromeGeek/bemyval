# 💘 Will You Be My Valentine?

An interactive, over-engineered Valentine's Day website where the **No button literally runs away from your cursor** for 8 attempts before finally giving in.

## ✨ Features

- 🎭 **4 Themed Modes** — Classic 💕, Terminal 💻, Cinematic 🎬, Arcade 👾
- 🏃 **Evasive No Button** — Teleports away 8 times with sarcastic messages before surrendering
- 🎆 **Confetti Celebration** — Canvas-confetti explosion when they say Yes
- ❤️ **3D Spinning Heart** — Three.js rendered finale
- ✨ **Sparkle Cursor Trail** — Because why not
- 📱 **Fully Responsive** — Works on phones, tablets, and desktops
- 🎯 **Custom Cursors** — Theme-specific cursor for each mode

## 🛠 Tech Stack

- **Build**: Python build system (`messages.py` → `build.py` → `template.html` → `dist/index.html`)
- **Frontend**: Tailwind CSS, GSAP 3.12, Three.js, Canvas-Confetti
- **Fonts**: Dancing Script, Quicksand, Fira Code, Playfair Display, Press Start 2P

## 🚀 Quick Start

```bash
python -m venv .venv
source .venv/bin/activate
python build.py --build-only
# Open dist/index.html in your browser
```

## 🌐 Deploy on Vercel

1. Push to GitHub
2. Import repo on [vercel.com](https://vercel.com)
3. Set **Output Directory** to `dist`
4. Deploy 🚀

## 💡 How It Works

1. You ask the big question 💕
2. They try to click **No** — but it escapes!
3. After 8 hilarious evasion attempts, **No** surrenders and becomes **Yes**
4. Confetti, 3D heart, and a sweet celebration screen 🎉

---

*Made with ❤️ (and way too much JavaScript) for Valentine's Day 2026*
