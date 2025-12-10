# 🎨 TEMPLATE SITE EXAMPLE

## Overview
This document shows the minimal structure needed for each of your 10 RTP websites after implementing the core repository system.

---

## 📁 Minimal Site Structure

```
website-1/
├── index.html              (Modified to use CDN)
├── styles.css              (Your custom design)
├── config.js               (Optional: Site-specific settings)
├── asset/
│   ├── 1.png              (Platform logo 1)
│   ├── 2.png              (Platform logo 2)
│   ├── 3.png              ... (Up to 17.png)
│   ├── banner/
│   │   ├── 1 (1).jpg      (Carousel images)
│   │   ├── 1 (2).jpg
│   │   ├── side-1.png     (Side banner)
│   │   └── ...
│   └── favicon/
│       └── favicon.jpg
├── images/                 (Optional: Can share from main site)
│   ├── HACKSAW/
│   ├── PG SOFT/
│   ├── Pragmatic Play/
│   └── ...
└── CNAME                   (Your custom domain)
```

---

## 📄 Modified index.html

### Key Changes:

**1. Script Tags (Bottom of file):**

```html
<!-- Scripts - CENTRALIZED FROM CORE REPOSITORY -->
<script src="https://YOUR-USERNAME.github.io/rtp-core/game-data.js"></script>
<script src="https://YOUR-USERNAME.github.io/rtp-core/provider_image_lists.js" onerror="console.log('Modo dinâmico')"></script>
<script src="https://YOUR-USERNAME.github.io/rtp-core/game_popularity.js"></script>
<script src="https://YOUR-USERNAME.github.io/rtp-core/script.js"></script>
</body>
</html>
```

**2. Optional: Add Config Script (Before core scripts):**

```html
<!-- Optional: Site-specific configuration -->
<script src="config.js"></script>

<!-- Core scripts from CDN -->
<script src="https://YOUR-USERNAME.github.io/rtp-core/game-data.js"></script>
<script src="https://YOUR-USERNAME.github.io/rtp-core/provider_image_lists.js"></script>
<script src="https://YOUR-USERNAME.github.io/rtp-core/game_popularity.js"></script>
<script src="https://YOUR-USERNAME.github.io/rtp-core/script.js"></script>
</body>
</html>
```

---

## ⚙️ Optional: config.js

Create this file for site-specific settings:

```javascript
/**
 * Site-Specific Configuration
 * This file contains unique settings for this website.
 * The core script.js reads these values if available.
 */

const SITE_CONFIG = {
    // ============================================
    // SITE IDENTITY
    // ============================================
    siteName: "POP REDE",           // Displayed in header
    siteVersion: "v8.9.1-BR",        // Version tag
    siteDomain: "poprede.com",       // Optional: for tracking
    
    // ============================================
    // PLATFORM LINKS (REQUIRED - Unique per site)
    // ============================================
    platforms: [
        { id: 1, url: 'https://popduqo.com?ch=23890' },
        { id: 2, url: 'https://popx5t.com?ch=13250' },
        { id: 3, url: 'https://popuptefa.com?ch=33323' },
        { id: 4, url: 'https://popbra.com/#/register?r_code=255862939718' },
        { id: 5, url: 'https://pop555.com/#/register?r_code=27363421531' },
        { id: 6, url: 'https://www.popbem66.com/#/register?r_code=62548100237' },
        { id: 7, url: 'https://poplua1.com/#/register?r_code=18527100158' },
        { id: 8, url: 'https://popkkk.com?code=252596' },
        { id: 9, url: 'https://pop678.com/#/register?r_code=84733330283' },
        { id: 10, url: 'https://pop888.com/#/register?r_code=82225748475' },
        { id: 11, url: 'https://26bet.com/?id=911719620' },
        { id: 12, url: 'https://poppg.com/#/register?r_code=87311374506' },
        { id: 13, url: 'https://q5gdw6.com?ch=2291' },
        { id: 14, url: 'https://popdezem.com?ch=30988' },
        { id: 15, url: 'https://9zqllv.com?ch=17356' },
        { id: 16, url: 'https://popceu.com/#/register?r_code=46223100109' },
        { id: 17, url: 'https://poplud.com?ch=30282' }
    ],
    
    // ============================================
    // SOCIAL LINKS (REQUIRED - Unique per site)
    // ============================================
    socialLinks: {
        telegram: 'https://poppremio.com/tg',
        whatsapp: 'https://pop-agent.com/wa'
    },
    
    // ============================================
    // BANNER CONFIGURATION (Optional)
    // ============================================
    banners: {
        carousel: [
            'asset/banner/1 (1).jpg',
            'asset/banner/1 (2).jpg',
            'asset/banner/1 (3).jpg',
            'asset/banner/1 (4).jpg',
            'asset/banner/1 (5).jpg',
            'asset/banner/1 (6).jpg',
            'asset/banner/1 (7).jpg'
        ],
        side: 'asset/banner/side-1.png',
        mainBannerLink: 'https://popduqo.com?ch=23890'
    },
    
    // ============================================
    // THEME COLORS (Optional - can use CSS instead)
    // ============================================
    theme: {
        primary: '#00f0ff',      // Cyan
        secondary: '#00ff88',    // Green
        accent: '#b800ff'        // Purple
    },
    
    // ============================================
    // ANALYTICS (Optional)
    // ============================================
    analytics: {
        googleAnalyticsId: 'G-PV01P9NMZL',
        enabled: true
    },
    
    // ============================================
    // FEATURE FLAGS (Optional)
    // ============================================
    features: {
        enableLoadMore: true,
        gamesPerPage: 100,
        enableCodeProtection: false,  // Disable right-click, etc.
        enableConsole: true
    }
};

// Export for core script to use
if (typeof window !== 'undefined') {
    window.SITE_CONFIG = SITE_CONFIG;
}
```

---

## 🎨 Custom styles.css

Each site keeps its own `styles.css` with unique:

- **Color schemes**
- **Fonts**
- **Button styles**
- **Layout adjustments**
- **Animations**

Example customization:

```css
/* Site 1: Blue/Cyan Theme (Default) */
:root {
    --accent-cyan: #00f0ff;
    --accent-green: #00ff88;
}

/* Site 2: Red/Orange Theme */
:root {
    --accent-cyan: #ff0055;
    --accent-green: #ff6600;
}

/* Site 3: Purple/Pink Theme */
:root {
    --accent-cyan: #b800ff;
    --accent-green: #ff00aa;
}
```

---

## 🖼️ Asset Files

### Platform Logos (asset/1.png - 17.png)
- Each site uses different platform logos
- Keep in `asset/` folder
- Named 1.png through 17.png

### Banner Images (asset/banner/)
- Carousel banners: `1 (1).jpg` through `1 (7).jpg`
- Side banner: `side-1.png`
- Custom per site

### Favicon (asset/favicon/)
- `favicon.jpg` - Unique per site

---

## 🌐 Custom Domain (CNAME)

```
your-custom-domain.com
```

---

## 📦 Game Images (Shared Option)

Instead of duplicating game images across 10 sites:

### Option 1: Share from Main Site
```javascript
// In config.js
const SITE_CONFIG = {
    imageBaseURL: 'https://main-site.github.io/images/'
};
```

Then core script constructs: `imageBaseURL + provider + '/' + imageName`

### Option 2: Use Same GitHub Repository
All sites can reference the same `/images/` folder if on same repo

### Option 3: CDN for Images
Upload images to a CDN and reference them:
```javascript
const SITE_CONFIG = {
    imageBaseURL: 'https://cdn.jsdelivr.net/gh/USER/rtp-images/'
};
```

---

## 🔧 How Core Script Uses Config

The core `script.js` checks for `window.SITE_CONFIG`:

```javascript
// In script.js (core repository)
const CONFIG = window.SITE_CONFIG || {
    // Default fallback values
    platforms: [...],
    socialLinks: {...}
};

// Use configuration
function generatePlatformCards() {
    CONFIG.platforms.forEach(platform => {
        // Use platform.url
    });
}
```

---

## 📋 Complete File Checklist

For each website, ensure you have:

### Required Files:
- ✅ `index.html` (modified to use CDN scripts)
- ✅ `styles.css` (your custom design)
- ✅ `asset/1.png` through `asset/17.png` (platform logos)
- ✅ `asset/banner/*.jpg` (carousel images)
- ✅ `asset/favicon/favicon.jpg`

### Optional Files:
- ⭕ `config.js` (site-specific settings)
- ⭕ `images/*` (or shared from main site)
- ⭕ `CNAME` (if using custom domain)

### NOT Needed (Served from Core):
- ❌ `script.js` → Use CDN
- ❌ `game-data.js` → Use CDN
- ❌ `provider_image_lists.js` → Use CDN
- ❌ `game_popularity.js` → Use CDN
- ❌ `animations.js` → Use CDN (if needed)

---

## 🚀 Quick Setup for New Site

```bash
# 1. Create new repository
mkdir website-2
cd website-2

# 2. Copy base files
cp ../website-1/index.html .
cp ../website-1/styles.css .

# 3. Create asset folders
mkdir -p asset/banner asset/favicon

# 4. Customize
# - Edit styles.css (colors, theme)
# - Add your platform logos (1.png - 17.png)
# - Add your banners
# - Create config.js with your platform links

# 5. Verify index.html uses CDN
# Check that script tags point to core repository

# 6. Deploy
git init
git add .
git commit -m "Initial commit - Site 2"
git push
```

---

## 🔄 Updates

### When Core Logic Changes:
✅ **NO ACTION NEEDED** - Automatic update from CDN

### When Design Changes:
1. Edit `styles.css`
2. Commit and push
3. Only this site updates

### When Platform Links Change:
1. Edit `config.js` (or directly in `index.html` if not using config)
2. Commit and push
3. Only this site updates

---

## ✨ Benefits Summary

| Aspect | Before | After |
|--------|--------|-------|
| **Files per site** | 10+ files | 3-5 files |
| **Code duplication** | 100% duplicated | 0% - Centralized |
| **Update effort** | Edit 10 sites | Edit 1 core |
| **Consistency** | Hard to maintain | Automatic |
| **Timezone sync** | ❌ Different per user | ✅ São Paulo time |
| **RTP accuracy** | ❌ Inconsistent | ✅ Identical globally |

---

**Next:** See `SETUP-GUIDE.md` for step-by-step migration instructions.

