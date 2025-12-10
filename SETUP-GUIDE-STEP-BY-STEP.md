# 🚀 STEP-BY-STEP SETUP GUIDE

## Complete Migration Guide for Multi-Site RTP Architecture

This guide will walk you through migrating your 10 RTP websites to use a centralized core repository with timezone synchronization.

---

## 📋 Prerequisites

- [ ] You have 10 RTP websites (or planning to create them)
- [ ] You have a GitHub account
- [ ] You understand basic Git commands
- [ ] You have access to all website repositories

**Time Required:** 2-3 hours for complete migration

---

## 🎯 Phase 1: Create Core Repository (30 minutes)

### Step 1.1: Create GitHub Repository

1. **Go to GitHub** → Click "New Repository"
2. **Repository name:** `rtp-core` (or your choice)
3. **Visibility:** Public (required for GitHub Pages CDN)
4. **Initialize:** ✅ Add README
5. Click **"Create repository"**

### Step 1.2: Prepare Core Files

On your local machine:

```bash
# Create new folder for core repository
mkdir rtp-core
cd rtp-core

# Initialize Git
git init
git remote add origin https://github.com/YOUR-USERNAME/rtp-core.git
```

### Step 1.3: Copy Core Files

Copy these files from your current website:

```bash
# From your main RTP website folder
cp script.js rtp-core/
cp game-data.js rtp-core/
cp provider_image_lists.js rtp-core/
cp game_popularity.js rtp-core/
cp animations.js rtp-core/  # if you have it
```

### Step 1.4: Upload to GitHub

```bash
cd rtp-core

# Stage files
git add .

# Commit
git commit -m "Initial commit: Core RTP system with timezone sync"

# Push to GitHub
git push -u origin main
```

### Step 1.5: Enable GitHub Pages

1. Go to your `rtp-core` repository on GitHub
2. Click **Settings** → **Pages**
3. Under "Source":
   - Branch: `main`
   - Folder: `/ (root)`
4. Click **Save**
5. Wait 2-5 minutes for deployment

### Step 1.6: Test Your CDN URLs

Your files are now available at:
```
https://YOUR-USERNAME.github.io/rtp-core/script.js
https://YOUR-USERNAME.github.io/rtp-core/game-data.js
https://YOUR-USERNAME.github.io/rtp-core/provider_image_lists.js
https://YOUR-USERNAME.github.io/rtp-core/game_popularity.js
```

**Test in browser:** Open these URLs to verify they load.

✅ **Phase 1 Complete!** Your core repository is live.

---

## 🎨 Phase 2: Test with One Website (30 minutes)

Let's migrate your first website as a test before doing all 10.

### Step 2.1: Choose Test Site

Pick your main/most important website to test with first.

### Step 2.2: Backup Current Files

```bash
cd your-website-1
mkdir backup
cp *.js backup/
cp *.html backup/
```

### Step 2.3: Create config.js (Optional but Recommended)

Create a new file `config.js`:

```bash
# Copy the example config
# Edit it with your platform links
nano config.js  # or use your text editor
```

Paste and customize the content from `config-example.js` (provided in previous files).

**Key sections to customize:**
- `siteName` → Your site name
- `platforms` → Your unique affiliate links
- `socialLinks` → Your Telegram/WhatsApp links

### Step 2.4: Update index.html

Find this section at the bottom of your `index.html`:

**BEFORE:**
```html
<!-- Scripts -->
<script src="game-data.js"></script>
<script src="provider_image_lists.js" onerror="console.log('Modo dinâmico')"></script>
<script src="game_popularity.js"></script>
<script src="script.js"></script>
</body>
</html>
```

**AFTER:**
```html
<!-- Site Configuration (Optional) -->
<script src="config.js"></script>

<!-- Scripts - Centralized from Core Repository -->
<script src="https://YOUR-USERNAME.github.io/rtp-core/game-data.js"></script>
<script src="https://YOUR-USERNAME.github.io/rtp-core/provider_image_lists.js" onerror="console.log('Modo dinâmico')"></script>
<script src="https://YOUR-USERNAME.github.io/rtp-core/game_popularity.js"></script>
<script src="https://YOUR-USERNAME.github.io/rtp-core/script.js"></script>
</body>
</html>
```

**Replace** `YOUR-USERNAME` with your actual GitHub username.

### Step 2.5: Test Locally

```bash
# If you have Python installed:
python -m http.server 8000

# Or if you have Node.js:
npx http-server
```

Open `http://localhost:8000` in your browser.

### Step 2.6: Verify Functionality

Check these items:
- [ ] Website loads correctly
- [ ] Games display properly
- [ ] RTP percentages show
- [ ] Timer counts down
- [ ] Platform modal opens
- [ ] Console shows "São Paulo" time logs

Open browser console (F12) and look for:
```
🕐 TimeSeed Debug (São Paulo): ...
📍 Hora Local: ...
📍 Hora São Paulo: ...
```

### Step 2.7: Commit and Deploy

If everything works:

```bash
git add index.html config.js
git commit -m "Migrate to centralized core repository"
git push
```

### Step 2.8: Verify Live Site

1. Wait 2-5 minutes for GitHub Pages to deploy
2. Visit your live website
3. Open console and verify timezone logs
4. Test all functionality

### Step 2.9: Compare with Telegram Bot

**CRITICAL TEST:**
1. Check RTP values on your website
2. Check RTP values from your Telegram bot
3. **They should MATCH exactly** (same games, same RTP%)

If they don't match:
- Verify your `script.js` in core repository has the timezone updates
- Check console for errors
- Ensure both are using 3-minute intervals

✅ **Phase 2 Complete!** Your first site is migrated and working.

---

## 🚀 Phase 3: Migrate Remaining 9 Sites (1-2 hours)

Now that you've tested successfully, migrate the rest quickly.

### Step 3.1: For Each Remaining Website

**Quick Migration Script:**

```bash
# Navigate to website
cd website-2

# Backup
mkdir backup
cp *.js backup/

# Create config.js
cp ../website-1/config.js .
# Edit platform links to be unique for this site
nano config.js

# Update index.html script tags
# (Same changes as Step 2.4)
nano index.html

# Commit
git add .
git commit -m "Migrate to centralized core + timezone sync"
git push
```

### Step 3.2: Customize Each Site

For each site, ensure you customize:

**In `config.js`:**
- [ ] `siteName` (if different)
- [ ] `platforms` array (MUST be unique per site)
- [ ] `socialLinks` (if different)
- [ ] `analytics.googleAnalyticsId` (if tracking separately)

**In `styles.css` (optional):**
- [ ] Color theme (make each site visually distinct)
- [ ] Fonts
- [ ] Custom layouts

**In `asset/` folder:**
- [ ] Platform logos (1.png - 17.png)
- [ ] Banner images
- [ ] Favicon

### Step 3.3: Verification Checklist

For each migrated site, verify:
- [ ] Site loads without errors
- [ ] RTP values display correctly
- [ ] Timer shows correct countdown
- [ ] Platform links open correct URLs
- [ ] Telegram/WhatsApp buttons work
- [ ] Console shows São Paulo timezone
- [ ] RTP matches Telegram bot

### Step 3.4: Optional - Delete Old Files

Once you verify a site works, you can delete old JS files:

```bash
# In each website folder
rm script.js
rm game-data.js  
rm provider_image_lists.js
rm game_popularity.js

# Keep config.js, index.html, styles.css, assets
git add -A
git commit -m "Clean up: Remove local JS files (now using CDN)"
git push
```

✅ **Phase 3 Complete!** All 10 sites are migrated.

---

## 🔄 Phase 4: Verify Synchronization (15 minutes)

### Step 4.1: Check Time Synchronization

**Test at the top of a 3-minute interval** (e.g., 10:00, 10:03, 10:06):

1. Open Website 1
2. Open Website 5  
3. Open Website 10
4. Note an RTP value for a specific game (e.g., "Gates of Olympus")

**Result:** All 3 websites should show the EXACT same RTP value.

### Step 4.2: Check Telegram Bot Sync

1. Request RTP from your Telegram bot
2. Compare with website values
3. **They must match exactly**

If they don't match:
- Check if bot uses same algorithm (it does from your Python code)
- Verify both use 3-minute intervals
- Check timezone is correctly set

### Step 4.3: Test Automatic Updates

1. Note current RTP for a game
2. Wait until next 3-minute interval (e.g., 10:03 → 10:06)
3. Watch console for update log
4. Verify RTP value changes

Expected console output:
```
═══════════════════════════════════════
🔄 ATUALIZAÇÃO DE RTP INICIADA (São Paulo Time)
⏰ TimeSeed NOVO: 278954583
📅 Minuto São Paulo: 6, Bloco: 6
🌎 Hora São Paulo: 10:06:00
🎮 Recalculando RTP de TODOS os jogos...
═══════════════════════════════════════
✅ RTP atualizado! Valores devem estar DIFERENTES agora.
✅ Todos os usuários no mundo veem os mesmos valores!
```

✅ **Phase 4 Complete!** Everything is synchronized.

---

## 🎯 Phase 5: Future Updates (Ongoing)

### Updating Core Logic

When you need to fix bugs or add features:

```bash
cd rtp-core

# Edit script.js (or other core files)
nano script.js

# Test changes
git add .
git commit -m "Fix: Improved RTP calculation"
git push

# Wait 2-5 minutes for GitHub Pages to update
# All 10 websites automatically get the update!
```

### Updating Individual Site Design

```bash
cd website-1

# Edit only design files
nano styles.css
# OR
# Update banners in asset/banner/
# OR  
nano config.js  # Change platform links

# Commit
git add .
git commit -m "Update: New blue theme"
git push

# Only this site changes, others unaffected
```

---

## 📊 Success Checklist

After completing all phases, verify:

### ✅ Core Repository
- [ ] `rtp-core` repository exists on GitHub
- [ ] GitHub Pages is enabled
- [ ] All 5 core files are accessible via CDN URLs
- [ ] `script.js` contains timezone synchronization code

### ✅ All 10 Websites
- [ ] Each site uses CDN script tags
- [ ] Each site has unique `config.js` (or unique platform links)
- [ ] Each site has custom `styles.css`
- [ ] Each site has unique assets (logos, banners, favicon)
- [ ] No duplicate local JS files (deleted after verification)

### ✅ Functionality
- [ ] All sites load without errors
- [ ] RTP values are identical across all sites (same game = same RTP)
- [ ] RTP values match Telegram bot
- [ ] Timer counts down correctly
- [ ] Auto-updates happen every 3 minutes
- [ ] Console shows São Paulo timezone

### ✅ Time Synchronization
- [ ] All users worldwide see same RTP values
- [ ] Values match regardless of user's local timezone
- [ ] Updates happen at exact same moment globally
- [ ] Aligned with Telegram bot timing

---

## 🐛 Troubleshooting

### Problem: Scripts don't load (404 errors)

**Solution:**
1. Verify GitHub Pages is enabled
2. Check URLs match exactly: `https://YOUR-USERNAME.github.io/rtp-core/script.js`
3. Wait 5 minutes after pushing to core repository
4. Hard refresh browser (Ctrl+Shift+R)

### Problem: RTP values don't match between sites

**Solution:**
1. Verify all sites use same CDN script URL
2. Clear browser cache on all sites
3. Check console for timezone logs - should all show "São Paulo"
4. Verify core `script.js` has timezone code

### Problem: RTP doesn't match Telegram bot

**Solution:**
1. Verify bot uses São Paulo timezone (your Python code does)
2. Check both use 3-minute intervals
3. Compare seed generation algorithm
4. Test at exactly same moment (top of 3-minute block)

### Problem: Updates don't propagate to sites

**Solution:**
1. Check GitHub Pages deployment status
2. Wait up to 10 minutes for CDN cache
3. Add cache-busting: `script.js?v=1.0.1`
4. Hard refresh browser

### Problem: Config not loading

**Solution:**
1. Verify `config.js` loads BEFORE core scripts
2. Check console for "✅ Site configuration loaded"
3. Verify syntax (no missing commas, brackets)
4. Check for JavaScript errors (F12 console)

---

## 📈 Performance Tips

### CDN Optimization

Use jsDelivr for faster delivery:
```html
<script src="https://cdn.jsdelivr.net/gh/YOUR-USERNAME/rtp-core@main/script.js"></script>
```

### Version Control

Add version numbers for cache control:
```html
<script src="https://YOUR-CDN/script.js?v=2.0.1"></script>
```

### Preloading

Add preload tags in `<head>`:
```html
<link rel="preload" href="https://YOUR-CDN/script.js" as="script">
```

---

## 🎉 Benefits After Migration

| Metric | Before | After |
|--------|--------|-------|
| **Time to update all sites** | 2-3 hours | 5 minutes |
| **Files to maintain** | 50 files | 5 files |
| **Code consistency** | Manual sync | Automatic |
| **Timezone issues** | ❌ Frequent | ✅ None |
| **RTP accuracy** | ❌ Varies by user | ✅ 100% consistent |
| **Bot synchronization** | ❌ Manual | ✅ Automatic |

---

## 📞 Support Resources

- **Core Repository Setup:** `CORE-REPOSITORY-SETUP.md`
- **Template Site Structure:** `TEMPLATE-SITE-EXAMPLE.md`
- **Config File Example:** `config-example.js`
- **GitHub Pages Docs:** https://pages.github.com/

---

## 🎯 Next Steps

1. [ ] Complete Phase 1 (Core Repository)
2. [ ] Complete Phase 2 (Test One Site)
3. [ ] Complete Phase 3 (Migrate All Sites)
4. [ ] Complete Phase 4 (Verify Sync)
5. [ ] Celebrate! 🎉

**Estimated Total Time:** 2-3 hours for complete migration

---

**Last Updated:** December 2025  
**System Version:** RTP v2.0  
**Timezone:** São Paulo (America/Sao_Paulo) UTC-3  
**Architecture:** Multi-Site Centralized Core

