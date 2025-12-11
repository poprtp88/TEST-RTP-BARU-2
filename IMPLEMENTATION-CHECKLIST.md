# ✅ IMPLEMENTATION CHECKLIST

## Step-by-Step Guide to Set Up Your Perfect CDN Architecture

Follow this checklist to implement the centralized CDN system where **EVERYTHING stays the same** except CSS and HTML.

---

## 📦 Phase 1: Prepare Core Repository

### ☑️ Step 1.1: Create Core Folder Locally

```powershell
# Create folder
cd "d:\WORK PROGRAM"
mkdir rtp-core
cd rtp-core
```

- [ ] Folder created

---

### ☑️ Step 1.2: Copy ALL Shared Files

```powershell
# Copy JavaScript files
copy "d:\WORK PROGRAM\rtp-main\TEST-RTP-BARU-2\script.js" .
copy "d:\WORK PROGRAM\rtp-main\TEST-RTP-BARU-2\game-data.js" .
copy "d:\WORK PROGRAM\rtp-main\TEST-RTP-BARU-2\provider_image_lists.js" .
copy "d:\WORK PROGRAM\rtp-main\TEST-RTP-BARU-2\game_popularity.js" .

# Copy images folder (ALL game images - 2.3GB)
xcopy "d:\WORK PROGRAM\rtp-main\TEST-RTP-BARU-2\images" "images\" /E /I /H

# Copy banner folder (carousel + side banner)
xcopy "d:\WORK PROGRAM\rtp-main\TEST-RTP-BARU-2\banner" "banner\" /E /I /H

# Copy asset folder (platform logos + favicon)
xcopy "d:\WORK PROGRAM\rtp-main\TEST-RTP-BARU-2\asset" "asset\" /E /I /H
```

- [ ] JavaScript files copied (4 files)
- [ ] Images folder copied (623 games, 6 providers)
- [ ] Banner folder copied (8 images)
- [ ] Asset folder copied (17 platform logos + favicon)

---

### ☑️ Step 1.3: Update script.js with CDN Paths

**Open:** `rtp-core/script.js`

**Add at the very top** (after initial comments):

```javascript
// ============================================
// CDN CONFIGURATION
// ============================================
const CDN_BASE = 'https://YOUR-USERNAME.github.io/rtp-core';

const CDN_PATHS = {
    images: `${CDN_BASE}/images`,
    banner: `${CDN_BASE}/banner`,
    asset: `${CDN_BASE}/asset`
};
```

**Find and replace image paths:**

Find: `images/${game.provider}/${game.imageName}`  
Replace with: `${CDN_PATHS.images}/${game.provider}/${game.imageName}`

Find: `asset/${platform.id}.png`  
Replace with: `${CDN_PATHS.asset}/${platform.id}.png`

- [ ] CDN configuration added
- [ ] Image paths updated
- [ ] Asset paths updated
- [ ] **IMPORTANT:** Replace `YOUR-USERNAME` with your GitHub username!

**OR** use the provided `script-cdn-template.js` as reference.

---

### ☑️ Step 1.4: Verify File Structure

Your `rtp-core` folder should look like this:

```
rtp-core/
├── script.js (CDN-enabled)
├── game-data.js
├── provider_image_lists.js
├── game_popularity.js
├── images/
│   ├── HACKSAW/
│   ├── PG SOFT/
│   ├── Play N' GO/
│   ├── Playtech/
│   ├── Pragmatic Play/
│   └── TADA/
├── banner/
│   ├── 1 (1).jpg
│   ├── ... (through 1 (7).jpg)
│   └── side-1.png
└── asset/
    ├── 1.png (through 17.png)
    └── favicon/
        └── favicon.jpg
```

- [ ] File structure verified

---

## 🌐 Phase 2: Upload Core to GitHub

### ☑️ Step 2.1: Create GitHub Repository

1. Go to: https://github.com/new
2. Repository name: `rtp-core`
3. **Make it PUBLIC** (required for GitHub Pages)
4. Don't add README, .gitignore, or license
5. Click "Create repository"

- [ ] GitHub repository created
- [ ] Repository is PUBLIC

---

### ☑️ Step 2.2: Initialize Git and Push

```powershell
cd "d:\WORK PROGRAM\rtp-core"

# Initialize Git
git init
git add .
git commit -m "Initial: Complete RTP core system with CDN support"

# Connect to GitHub (replace YOUR-USERNAME!)
git remote add origin https://github.com/YOUR-USERNAME/rtp-core.git
git branch -M main

# Push to GitHub (may take 5-10 minutes due to large files)
git push -u origin main
```

- [ ] Git initialized
- [ ] Files pushed to GitHub
- [ ] Verify all files uploaded on GitHub website

---

### ☑️ Step 2.3: Enable GitHub Pages

1. Go to your `rtp-core` repository on GitHub
2. Click **Settings** (top right)
3. Scroll to **Pages** (left sidebar)
4. Under "Source":
   - Branch: `main`
   - Folder: `/ (root)`
5. Click **Save**
6. Wait 2-5 minutes for deployment

- [ ] GitHub Pages enabled
- [ ] Deployment complete (check for green checkmark)

---

### ☑️ Step 2.4: Test CDN URLs

**Your CDN base URL:**
```
https://YOUR-USERNAME.github.io/rtp-core/
```

**Test these URLs in your browser** (replace YOUR-USERNAME):

✅ Script: `https://YOUR-USERNAME.github.io/rtp-core/script.js`  
✅ Game data: `https://YOUR-USERNAME.github.io/rtp-core/game-data.js`  
✅ Game image: `https://YOUR-USERNAME.github.io/rtp-core/images/Pragmatic%20Play/vs20olympgate.jpg`  
✅ Banner: `https://YOUR-USERNAME.github.io/rtp-core/banner/1%20(1).jpg`  
✅ Logo: `https://YOUR-USERNAME.github.io/rtp-core/asset/1.png`  
✅ Favicon: `https://YOUR-USERNAME.github.io/rtp-core/asset/favicon/favicon.jpg`

- [ ] All CDN URLs load successfully
- [ ] No 404 errors
- [ ] Images display correctly

---

## 🎨 Phase 3: Create First Website

### ☑️ Step 3.1: Create Website Folder

```powershell
cd "d:\WORK PROGRAM"
mkdir website-1
cd website-1
```

- [ ] Website folder created

---

### ☑️ Step 3.2: Create index.html

**Copy your current HTML structure** but update script and asset references:

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Site 1 - Sistema RTP</title>
    
    <!-- LOCAL CSS (your custom design) -->
    <link rel="stylesheet" href="styles.css">
    
    <!-- CDN: Favicon -->
    <link rel="icon" href="https://YOUR-USERNAME.github.io/rtp-core/asset/favicon/favicon.jpg">
</head>

<body>
    <!-- Your HTML structure here -->
    
    <!-- CDN: Banners -->
    <img src="https://YOUR-USERNAME.github.io/rtp-core/banner/1%20(1).jpg">
    <!-- ... more banners ... -->
    
    <!-- CDN: Scripts -->
    <script src="https://YOUR-USERNAME.github.io/rtp-core/game-data.js"></script>
    <script src="https://YOUR-USERNAME.github.io/rtp-core/provider_image_lists.js"></script>
    <script src="https://YOUR-USERNAME.github.io/rtp-core/game_popularity.js"></script>
    <script src="https://YOUR-USERNAME.github.io/rtp-core/script.js"></script>
</body>
</html>
```

- [ ] index.html created
- [ ] All CDN URLs use correct GitHub username
- [ ] Banner paths updated to CDN
- [ ] Script tags updated to CDN
- [ ] Favicon updated to CDN

**OR** use `index-cdn-template.html` as reference.

---

### ☑️ Step 3.3: Create styles.css

```css
/* Custom design for Website 1 */

:root {
    /* YOUR CUSTOM COLORS */
    --accent-cyan: #00f0ff;      /* Main color */
    --accent-green: #00ff88;     /* Secondary */
    --bg-primary: #050a1e;       /* Background */
}

/* Copy your CSS here */
/* This is where you customize the look! */
```

- [ ] styles.css created
- [ ] Custom colors defined
- [ ] Design customizations added

---

### ☑️ Step 3.4: Test Locally

```powershell
# Start local server
python -m http.server 8000

# OR with Node.js:
# npx http-server
```

Open: http://localhost:8000

**Test checklist:**
- [ ] Website loads without errors
- [ ] Games display with images from CDN
- [ ] Banners show from CDN
- [ ] Platform logos load from CDN
- [ ] Timer counts down
- [ ] RTP values show correctly
- [ ] No console errors (F12)

---

### ☑️ Step 3.5: Deploy Website 1

```powershell
cd "d:\WORK PROGRAM\website-1"

git init
git add .
git commit -m "Initial: Website 1 - Blue theme"

# Create repo on GitHub first: website-1
git remote add origin https://github.com/YOUR-USERNAME/website-1.git
git branch -M main
git push -u origin main

# Enable GitHub Pages for website-1 too
```

- [ ] Git initialized
- [ ] Pushed to GitHub
- [ ] GitHub Pages enabled for website-1
- [ ] Website live and working

---

## 🚀 Phase 4: Create Remaining Websites

### ☑️ Step 4.1: Create Website 2

```powershell
# Copy Website 1 as template
xcopy "d:\WORK PROGRAM\website-1" "d:\WORK PROGRAM\website-2" /E /I /H
cd "d:\WORK PROGRAM\website-2"

# Edit styles.css (change colors to Red theme)
# Edit index.html (change title, SEO tags if needed)
```

**In styles.css, change colors:**
```css
:root {
    --accent-cyan: #ff0055;      /* Red theme */
    --accent-green: #ff6600;
}
```

- [ ] Website 2 folder created
- [ ] styles.css customized (red theme)
- [ ] index.html title updated

```powershell
git init
git add .
git commit -m "Initial: Website 2 - Red theme"
git remote add origin https://github.com/YOUR-USERNAME/website-2.git
git branch -M main
git push -u origin main

# Enable GitHub Pages
```

- [ ] Website 2 deployed
- [ ] GitHub Pages enabled
- [ ] Site working with red theme

---

### ☑️ Step 4.2: Repeat for Websites 3-10

For each website (3, 4, 5, 6, 7, 8, 9, 10):

1. Copy website-1 as template
2. Edit `styles.css` → Change colors/theme
3. Edit `index.html` → Change title, SEO (optional)
4. Edit `CNAME` → Add custom domain (optional)
5. Push to GitHub
6. Enable GitHub Pages

**Theme Suggestions:**
- Website 3: Purple (#b800ff, #ff00aa)
- Website 4: Green (#00ff00, #00cc00)
- Website 5: Orange (#ff6600, #ffaa00)
- Website 6: Pink (#ff1493, #ff69b4)
- Website 7: Gold (#ffd700, #ffaa00)
- Website 8: Cyan (#00ffff, #00ccff)
- Website 9: Lime (#00ff88, #00dd66)
- Website 10: Teal (#008080, #00a0a0)

**Checklist:**
- [ ] Website 3 deployed
- [ ] Website 4 deployed
- [ ] Website 5 deployed
- [ ] Website 6 deployed
- [ ] Website 7 deployed
- [ ] Website 8 deployed
- [ ] Website 9 deployed
- [ ] Website 10 deployed

---

## ✅ Phase 5: Final Verification

### ☑️ Step 5.1: Test All Sites

For EACH of your 10 websites, verify:

**Website 1:**
- [ ] Loads correctly
- [ ] Shows games with CDN images
- [ ] RTP values calculate correctly
- [ ] Timer works
- [ ] Platform modal opens
- [ ] Unique design/colors

**Website 2:**
- [ ] All checks above
- [ ] Different colors than Website 1

**... (Repeat for all 10 websites)**

---

### ☑️ Step 5.2: Test Synchronization

1. Open Website 1, 5, and 10 simultaneously
2. Find the same game (e.g., "Gates of Olympus")
3. **Check:** All 3 sites show SAME RTP value
4. **Check:** All 3 sites show SAME game images
5. **Check:** All 3 sites show SAME banners

- [ ] RTP values match across all sites
- [ ] Images load from CDN on all sites
- [ ] Banners same on all sites
- [ ] Different designs per site

---

### ☑️ Step 5.3: Test Update Workflow

**Test 1: Update Core (affects all sites)**

```powershell
cd "d:\WORK PROGRAM\rtp-core"

# Make a small change to script.js (add console.log)
# Add at the end: console.log('✅ Core v2.0.1');

git add script.js
git commit -m "Update: Version bump to 2.0.1"
git push

# Wait 2-5 minutes
# Check Website 1, 5, 10 - all should show new console.log
```

- [ ] Core update pushed
- [ ] All sites show update after 2-5 minutes

**Test 2: Update One Site (affects only that site)**

```powershell
cd "d:\WORK PROGRAM\website-3"

# Change color in styles.css
# Example: --accent-cyan: #0000ff;

git add styles.css
git commit -m "Update: Changed to pure blue"
git push

# Check: Only Website 3 changed, others unchanged
```

- [ ] Website 3 design updated
- [ ] Other websites unchanged

---

## 🎓 Phase 6: Documentation

### ☑️ Step 6.1: Create README in Core Repo

In `rtp-core/README.md`:

```markdown
# RTP Core System

Central repository for RTP website system.

## CDN URLs
- Base: https://YOUR-USERNAME.github.io/rtp-core/
- Scripts: /script.js, /game-data.js, etc.
- Images: /images/PROVIDER/game.jpg
- Banners: /banner/1 (1).jpg
- Assets: /asset/1.png

## Websites Using This Core
1. Website 1 (Blue)
2. Website 2 (Red)
... (list all 10)

## To Update
Edit files → Push to GitHub → Wait 2-5 min → All sites updated
```

- [ ] README created in core
- [ ] URLs documented

---

### ☑️ Step 6.2: Save Your GitHub URLs

Create a text file with all your URLs for easy reference:

```
CORE CDN:
https://YOUR-USERNAME.github.io/rtp-core/

WEBSITES:
1. https://YOUR-USERNAME.github.io/website-1/
2. https://YOUR-USERNAME.github.io/website-2/
... (all 10)
```

- [ ] URL list saved

---

## 🎉 Final Checklist

### ✅ Core Repository
- [ ] Created and uploaded to GitHub
- [ ] GitHub Pages enabled
- [ ] All files accessible via CDN
- [ ] script.js updated with CDN paths

### ✅ Website Repositories (All 10)
- [ ] All created and uploaded
- [ ] Each has unique styles.css
- [ ] Each has index.html with CDN references
- [ ] Each has GitHub Pages enabled
- [ ] Each works independently

### ✅ Functionality
- [ ] All sites load correctly
- [ ] Games display from CDN images
- [ ] Banners load from CDN
- [ ] RTP values synchronized across sites
- [ ] Each site has unique design
- [ ] Timer works on all sites
- [ ] Platform modals work on all sites

### ✅ Architecture
- [ ] EVERYTHING shared in core repo
- [ ] ONLY CSS and HTML in each website
- [ ] CDN paths work correctly
- [ ] Updates to core affect all sites
- [ ] Updates to sites only affect that site

---

## 💡 Maintenance Reference

### Daily:
- No action needed! ✅

### When You Want to Fix RTP Bug:
```powershell
cd rtp-core
# Edit script.js
git push
# Wait 5 min → ALL 10 sites fixed!
```

### When You Want to Change One Site's Design:
```powershell
cd website-5
# Edit styles.css
git push
# Only Website 5 changes!
```

### When You Want to Add New Game:
```powershell
cd rtp-core
# Add to images/Provider/
# Edit game-data.js
git push
# Wait 5 min → ALL 10 sites show new game!
```

---

## 🏆 SUCCESS!

You now have:
- ✅ 1 Core repository (2.5GB)
- ✅ 10 Website repositories (~10KB each)
- ✅ Perfect CDN architecture
- ✅ 90% storage savings
- ✅ 95% time savings on updates
- ✅ Zero code duplication
- ✅ Easy maintenance

**Total Time Investment:** 2-3 hours  
**Time Saved Per Update:** Forever! 🚀

---

**Implementation Date:** December 10, 2025  
**Architecture:** Fully Centralized Core + Lightweight Sites  
**Status:** ✅ Production Ready  
**Next:** Enjoy easy maintenance!

