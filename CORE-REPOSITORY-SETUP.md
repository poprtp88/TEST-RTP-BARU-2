# 🚀 CORE REPOSITORY SETUP GUIDE

## Overview
This guide explains how to set up a centralized core repository that powers multiple RTP websites with different designs.

---

## 📁 Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    CORE REPOSITORY                          │
│              (Centralized Logic - One Source)               │
│                                                             │
│  ├── script.js              (Main RTP logic + timezone)    │
│  ├── game-data.js           (Game database)                │
│  ├── provider_image_lists.js (Provider images)             │
│  ├── game_popularity.js     (Popularity rankings)          │
│  └── animations.js          (Optional effects)             │
└─────────────────────────────────────────────────────────────┘
                            ↓ ↓ ↓
        ┌──────────────┬────────────────┬────────────────┐
        │              │                │                │
   ┌────▼────┐   ┌────▼────┐      ┌────▼────┐      ┌────▼────┐
   │ Site 1  │   │ Site 2  │ ...  │ Site 9  │      │ Site 10 │
   │(Design) │   │(Design) │      │(Design) │      │(Design) │
   └─────────┘   └─────────┘      └─────────┘      └─────────┘
```

---

## 🎯 Problem Solved

**Before:** 10 repositories × 5 core files = 50 files to update when fixing a bug  
**After:** 1 core repository × 5 files = 5 files to update, affects all sites instantly

---

## 📦 Step 1: Create Core Repository

### Option A: GitHub Pages (Recommended - Free)

1. **Create a new repository:**
   - Name: `rtp-core` (or any name)
   - Public repository (required for GitHub Pages)

2. **Upload these files:**
   ```
   rtp-core/
   ├── script.js               ✅ (Already timezone-synchronized!)
   ├── game-data.js
   ├── provider_image_lists.js
   ├── game_popularity.js
   ├── animations.js
   └── README.md
   ```

3. **Enable GitHub Pages:**
   - Go to repository Settings → Pages
   - Source: Deploy from branch
   - Branch: main → /root
   - Save

4. **Your CDN URLs will be:**
   ```
   https://YOUR-USERNAME.github.io/rtp-core/script.js
   https://YOUR-USERNAME.github.io/rtp-core/game-data.js
   https://YOUR-USERNAME.github.io/rtp-core/provider_image_lists.js
   https://YOUR-USERNAME.github.io/rtp-core/game_popularity.js
   ```

### Option B: jsDelivr CDN (Faster, Free)

jsDelivr automatically serves GitHub files as CDN:
```
https://cdn.jsdelivr.net/gh/YOUR-USERNAME/rtp-core@main/script.js
https://cdn.jsdelivr.net/gh/YOUR-USERNAME/rtp-core@main/game-data.js
```

**Advantage:** Faster global delivery, automatic caching

---

## 🌐 Step 2: Modify Each Website

### In each of your 10 websites' `index.html`:

**BEFORE (Local files):**
```html
<!-- Scripts -->
<script src="game-data.js"></script>
<script src="provider_image_lists.js"></script>
<script src="game_popularity.js"></script>
<script src="script.js"></script>
```

**AFTER (CDN files):**
```html
<!-- Scripts - Loaded from Core Repository -->
<script src="https://YOUR-USERNAME.github.io/rtp-core/game-data.js"></script>
<script src="https://YOUR-USERNAME.github.io/rtp-core/provider_image_lists.js" onerror="console.log('Modo dinâmico')"></script>
<script src="https://YOUR-USERNAME.github.io/rtp-core/game_popularity.js"></script>
<script src="https://YOUR-USERNAME.github.io/rtp-core/script.js"></script>
```

### Each Website Now Only Needs:

```
website-1/
├── index.html       (Structure - references core CDN)
├── styles.css       (Custom design/theme)
├── asset/           (Custom banners, images, favicon)
│   ├── 1.png        (Platform logos)
│   ├── 2.png
│   ├── banner/
│   └── favicon/
├── images/          (Game images - can share same folder)
└── CNAME            (Custom domain)
```

---

## ✅ Benefits

### ✨ Single Source of Truth
- Update `script.js` once → All 10 sites updated instantly
- Fix a bug once → Fixed everywhere
- Add a feature once → Available on all sites

### 🎨 Design Freedom
- Each site keeps unique:
  - Color themes (CSS)
  - Banners
  - Logos
  - Platform links
  - Layout structure

### 🕐 Synchronized Time
- ✅ All users worldwide see same RTP percentages
- ✅ Synchronized with Telegram bot
- ✅ Uses São Paulo timezone (America/Sao_Paulo)
- ✅ No more timezone conflicts

### 🚀 Easy Maintenance
- No need to copy-paste code between repositories
- Version control for core logic
- Test once, deploy to all

---

## 🔧 Advanced: Site-Specific Configuration

### Option 1: Config File (Per Site)

Create `config.js` in each website:

```javascript
// config.js - Site-specific settings
const SITE_CONFIG = {
    // Site Identity
    siteName: "POP REDE",
    siteVersion: "v8.9.1-BR",
    
    // Theming (optional - can use CSS instead)
    theme: {
        primaryColor: "#00f0ff",
        secondaryColor: "#00ff88"
    },
    
    // Platform Links (unique per site)
    platforms: [
        { id: 1, url: 'https://popduqo.com?ch=23890' },
        { id: 2, url: 'https://popx5t.com?ch=13250' },
        // ... your unique platform links
    ],
    
    // Social Links
    socialLinks: {
        telegram: 'https://poppremio.com/tg',
        whatsapp: 'https://pop-agent.com/wa'
    }
};
```

Then in `index.html`, load config BEFORE core scripts:
```html
<script src="config.js"></script>
<script src="https://YOUR-CDN/rtp-core/script.js"></script>
```

The core `script.js` can check if `SITE_CONFIG` exists and use it.

### Option 2: Data Attributes (Simple)

In `index.html`:
```html
<body data-site-name="POP REDE" data-site-version="v8.9.1">
```

Core script reads these attributes.

---

## 🔄 Update Workflow

### When You Need to Update Logic:

1. **Edit core repository:**
   ```bash
   cd rtp-core
   # Edit script.js
   git add script.js
   git commit -m "Fix: RTP calculation bug"
   git push
   ```

2. **GitHub Pages updates automatically (2-5 minutes)**

3. **All 10 websites get the update:**
   - Users refresh → Get new version
   - No manual deployment needed

### When You Need to Update Design:

1. **Edit specific website:**
   ```bash
   cd website-1
   # Edit styles.css
   git add styles.css
   git commit -m "Update: New color theme"
   git push
   ```

2. **Only that website changes**

---

## 🎯 Testing Before Deployment

### Test Locally First:
```html
<!-- In index.html, temporarily use local file -->
<script src="script.js"></script>

<!-- When ready, switch to CDN -->
<script src="https://YOUR-CDN/script.js"></script>
```

### Version Control (Advanced):
```html
<!-- Use specific version/commit -->
<script src="https://cdn.jsdelivr.net/gh/USER/rtp-core@v1.0.0/script.js"></script>

<!-- Or use latest -->
<script src="https://cdn.jsdelivr.net/gh/USER/rtp-core@main/script.js"></script>
```

---

## 📊 Migration Checklist

For each of your 10 websites:

- [ ] Create `rtp-core` repository
- [ ] Upload core JavaScript files
- [ ] Enable GitHub Pages or note jsDelivr URLs
- [ ] Update `index.html` in Website 1 to use CDN
- [ ] Test Website 1 thoroughly
- [ ] Verify RTP values match Telegram bot
- [ ] Update remaining 9 websites
- [ ] Delete old local JS files (keep backups!)
- [ ] Document your CDN URLs for reference

---

## 🚨 Important Notes

### Caching
- GitHub Pages/jsDelivr cache files (good for performance)
- Updates may take 2-10 minutes to propagate
- For instant updates, add version query: `script.js?v=1.2.3`

### Fallback
Keep a backup local copy in case CDN is down:
```html
<script src="https://CDN/script.js" 
        onerror="this.src='script.js'"></script>
```

### CORS (Cross-Origin)
- GitHub Pages: ✅ CORS enabled by default
- jsDelivr: ✅ CORS enabled by default
- Custom server: May need CORS headers

---

## 🎉 Result

**Before:**
- 10 repositories with duplicate code
- Update 1 file = Edit in 10 places
- Risk of version mismatch
- Timezone inconsistencies

**After:**
- 1 core repository + 10 design repositories
- Update 1 file = Update everywhere instantly
- Single source of truth
- ✅ Synchronized São Paulo timezone
- ✅ All users see identical RTP values

---

## 📞 Next Steps

1. See `TEMPLATE-SITE-EXAMPLE.md` for site structure
2. See `SETUP-GUIDE.md` for step-by-step instructions
3. Test with one site first before migrating all 10

---

**Last Updated:** December 2025  
**Timezone:** São Paulo (America/Sao_Paulo) - UTC-3  
**System:** RTP v2.0 - Multi-Site Architecture

