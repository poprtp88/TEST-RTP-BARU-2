# ⚡ QUICK START GUIDE

## 🎯 TL;DR - Get Started in 5 Minutes

Your system is ready! Here's the fastest way to get started.

---

## ✅ Problem 1: Timezone Fixed (Already Done!)

Your `script.js` is **already updated** with São Paulo timezone synchronization.

### Test Right Now:

1. **Open your website**
2. **Press F12** (open console)
3. **Look for these logs:**
   ```
   🕐 TimeSeed Debug (São Paulo): ...
   📍 Hora Local: 14:06:35
   📍 Hora São Paulo: 10:06:35
   ```

4. **Compare with Telegram bot:**
   - Check an RTP value on website (e.g., "Gates of Olympus: 87%")
   - Request same game from Telegram bot
   - **They should match exactly!**

**✅ If they match → Problem 1 is SOLVED!**

---

## 🏗️ Problem 2: Multi-Site Setup (Optional)

Want to manage 10 websites easily? Follow these steps:

### Step 1: Create Core Repository (10 minutes)

```bash
# 1. Create GitHub repo named 'rtp-core'
# 2. Upload these files:
#    - script.js (already updated!)
#    - game-data.js
#    - provider_image_lists.js
#    - game_popularity.js
# 3. Enable GitHub Pages in Settings
# 4. Your CDN URL: https://YOUR-USERNAME.github.io/rtp-core/
```

### Step 2: Update One Website (5 minutes)

In your `index.html`, change bottom scripts from:

```html
<!-- OLD -->
<script src="script.js"></script>
```

To:

```html
<!-- NEW -->
<script src="https://YOUR-USERNAME.github.io/rtp-core/script.js"></script>
<script src="https://YOUR-USERNAME.github.io/rtp-core/game-data.js"></script>
<script src="https://YOUR-USERNAME.github.io/rtp-core/provider_image_lists.js"></script>
<script src="https://YOUR-USERNAME.github.io/rtp-core/game_popularity.js"></script>
```

### Step 3: Test & Repeat (15 minutes)

- Test that website works
- Repeat for remaining 9 websites
- **Done!** Now updating `script.js` once updates all 10 sites

---

## 📚 Full Documentation

| Need | Read This |
|------|-----------|
| **Quick test timezone** | This file (you're here!) |
| **Understand architecture** | `CORE-REPOSITORY-SETUP.md` |
| **See site examples** | `TEMPLATE-SITE-EXAMPLE.md` |
| **Configure each site** | `config-example.js` |
| **Step-by-step migration** | `SETUP-GUIDE-STEP-BY-STEP.md` |
| **See what was done** | `README-IMPLEMENTATION.md` |

---

## 🎯 Decision Tree

**Start Here:**

```
Do your RTP values sync with Telegram bot?
├─ NO → Check console for "São Paulo" logs
│       See README-IMPLEMENTATION.md for details
│
└─ YES → Great! Timezone is working!
         
         Do you want easy multi-site management?
         ├─ NO → You're done! Keep using as-is
         │
         └─ YES → Follow Step 1-3 above
                  OR read SETUP-GUIDE-STEP-BY-STEP.md
```

---

## ✨ Benefits You Get

### Timezone Sync (Already Active):
- ✅ All users see same RTP values globally
- ✅ Perfect sync with Telegram bot
- ✅ No more timezone confusion

### Multi-Site (Optional Setup):
- ✅ Update 1 file → All 10 sites update
- ✅ Fix bug once instead of 10 times
- ✅ Zero code duplication
- ✅ Each site keeps unique design

---

## 🚀 Start Testing Now!

**Press F12 on your website and check for São Paulo timezone logs!**

Then decide if you want to set up the multi-site architecture.

---

**Need help? Read:** `README-IMPLEMENTATION.md`  
**Ready to migrate?** Read: `SETUP-GUIDE-STEP-BY-STEP.md`

