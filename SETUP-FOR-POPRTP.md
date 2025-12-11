# 🚀 SETUP GUIDE FOR POPRTP.COM

## Your Repository & Domain Information

✅ **GitHub Repository:** https://github.com/poprtp88/TEST-RTP-BARU-2  
✅ **Website Domain:** https://poprtp.com/  
✅ **GitHub Username:** poprtp88  

---

## 📋 CRITICAL ADJUSTMENTS NEEDED

You need to update these placeholders in your files:

### 1. Replace `YOUR-USERNAME` → `poprtp88`
### 2. Replace `yourwebsite.com` → `poprtp.com`

---

## 🔧 STEP-BY-STEP ADJUSTMENTS

### **Phase 1: Enable GitHub Pages for CDN**

1. **Go to your repository:**  
   https://github.com/poprtp88/TEST-RTP-BARU-2

2. **Click Settings** (top right)

3. **Click Pages** (left sidebar)

4. **Under "Source":**
   - Branch: `main`
   - Folder: `/ (root)`
   - Click **Save**

5. **Wait 2-5 minutes for deployment**

6. **Your CDN URL will be:**
   ```
   https://poprtp88.github.io/TEST-RTP-BARU-2/
   ```

✅ **Test CDN URLs:**
- Script: https://poprtp88.github.io/TEST-RTP-BARU-2/script.js
- Image: https://poprtp88.github.io/TEST-RTP-BARU-2/images/Pragmatic%20Play/vs20olympgate.jpg
- Banner: https://poprtp88.github.io/TEST-RTP-BARU-2/banner/1%20(1).jpg

---

### **Phase 2: Update SEO Files**

#### **File: index.html**

Find and replace ALL instances:

**Find:** `yourwebsite.com`  
**Replace:** `poprtp.com`

**Locations to update:**
- Line ~20: Canonical URL
- Lines ~23-40: Open Graph URLs (og:url, og:image)
- Lines ~31-36: Twitter Card URLs
- JSON-LD structured data at bottom (2 blocks)

**PowerShell Command:**
```powershell
cd "d:\WORK PROGRAM\rtp-main\TEST-RTP-BARU-2"
(Get-Content index.html) -replace 'yourwebsite.com', 'poprtp.com' | Set-Content index.html
```

#### **File: sitemap.xml**

**Find:** `yourwebsite.com`  
**Replace:** `poprtp.com`

**PowerShell Command:**
```powershell
(Get-Content sitemap.xml) -replace 'yourwebsite.com', 'poprtp.com' | Set-Content sitemap.xml
```

#### **File: robots.txt**

**Find:** `yourwebsite.com`  
**Replace:** `poprtp.com`

**PowerShell Command:**
```powershell
(Get-Content robots.txt) -replace 'yourwebsite.com', 'poprtp.com' | Set-Content robots.txt
```

---

### **Phase 3: Update Script with CDN Paths**

#### **File: script.js**

Add this at the **very top** of script.js (after comments):

```javascript
// ============================================
// CDN CONFIGURATION FOR POPRTP.COM
// ============================================

const CDN_BASE = 'https://poprtp88.github.io/TEST-RTP-BARU-2';

const CDN_PATHS = {
    images: `${CDN_BASE}/images`,
    banner: `${CDN_BASE}/banner`,
    asset: `${CDN_BASE}/asset`
};

console.log('✅ CDN Configuration loaded for poprtp.com');
console.log('📦 Assets loading from:', CDN_BASE);
```

Then **find and replace** image paths in your script.js:

**Find:**
```javascript
imagePath = `images/${provider}/${imageName}`
```

**Replace with:**
```javascript
imagePath = `${CDN_PATHS.images}/${provider}/${imageName}`
```

**Find:**
```javascript
logoPath = `asset/${platform.id}.png`
```

**Replace with:**
```javascript
logoPath = `${CDN_PATHS.asset}/${platform.id}.png`
```

**Reference:** Use `script-cdn-template.js` as a guide

---

### **Phase 4: Update HTML Banner/Asset References**

#### **File: index.html**

Update banner image sources:

**Find:**
```html
<img src="asset/banner/1 (1).jpg">
```

**Replace with:**
```html
<img src="https://poprtp88.github.io/TEST-RTP-BARU-2/banner/1%20(1).jpg">
```

**Do this for ALL 7 carousel banners:**
- 1 (1).jpg through 1 (7).jpg
- side-1.png (side banner)

Update favicon:

**Find:**
```html
<link rel="icon" href="asset/favicon/favicon.jpg">
```

**Replace with:**
```html
<link rel="icon" href="https://poprtp88.github.io/TEST-RTP-BARU-2/asset/favicon/favicon.jpg">
```

---

### **Phase 5: Commit and Push Changes**

```powershell
cd "d:\WORK PROGRAM\rtp-main\TEST-RTP-BARU-2"

# Stage all changes
git add .

# Commit
git commit -m "Update: Configure for poprtp.com with CDN paths"

# Push to GitHub
git push
```

---

## 🧪 TESTING YOUR SETUP

### **Test 1: Verify CDN Works**

Open these URLs in your browser:

✅ **Script:**  
https://poprtp88.github.io/TEST-RTP-BARU-2/script.js

✅ **Game Image:**  
https://poprtp88.github.io/TEST-RTP-BARU-2/images/Pragmatic%20Play/vs20olympgate.jpg

✅ **Banner:**  
https://poprtp88.github.io/TEST-RTP-BARU-2/banner/1%20(1).jpg

✅ **Platform Logo:**  
https://poprtp88.github.io/TEST-RTP-BARU-2/asset/1.png

**All should load successfully!**

---

### **Test 2: Verify Website Loads**

1. Open: https://poprtp.com/
2. Press **F12** (Developer Console)
3. Check for:
   - ✅ No 404 errors
   - ✅ Images loading from CDN
   - ✅ Console shows "CDN Configuration loaded"
   - ✅ Games display correctly
   - ✅ RTP values show

---

### **Test 3: SEO Verification**

**Google Rich Results Test:**  
https://search.google.com/test/rich-results

Enter: `https://poprtp.com/`

Check for:
- ✅ No errors
- ✅ Structured data found
- ✅ WebApplication schema detected

**Mobile-Friendly Test:**  
https://search.google.com/test/mobile-friendly

Enter: `https://poprtp.com/`

Should show: ✅ **Page is mobile-friendly**

---

## 📊 COMPLETE URL REFERENCE

### **Your CDN Base URL:**
```
https://poprtp88.github.io/TEST-RTP-BARU-2/
```

### **Asset URLs:**
```
Scripts:
- https://poprtp88.github.io/TEST-RTP-BARU-2/script.js
- https://poprtp88.github.io/TEST-RTP-BARU-2/game-data.js
- https://poprtp88.github.io/TEST-RTP-BARU-2/provider_image_lists.js
- https://poprtp88.github.io/TEST-RTP-BARU-2/game_popularity.js

Images:
- https://poprtp88.github.io/TEST-RTP-BARU-2/images/{PROVIDER}/{game}.jpg

Banners:
- https://poprtp88.github.io/TEST-RTP-BARU-2/banner/1%20(1).jpg
- https://poprtp88.github.io/TEST-RTP-BARU-2/banner/1%20(2).jpg
- ... (through 1 (7).jpg)
- https://poprtp88.github.io/TEST-RTP-BARU-2/banner/side-1.png

Assets:
- https://poprtp88.github.io/TEST-RTP-BARU-2/asset/1.png (through 17.png)
- https://poprtp88.github.io/TEST-RTP-BARU-2/asset/favicon/favicon.jpg
```

---

## 🎯 USING THIS AS CORE REPOSITORY

### **Option A: Use Current Repository as Core**

Your repository **TEST-RTP-BARU-2** can serve as your core!

✅ **Advantages:**
- Already uploaded
- GitHub Pages already set up
- All files in place

**How to Use:**
1. This repo stays as your **CORE**
2. Create new repos for each website design:
   - `poprtp-site-1` (Blue theme)
   - `poprtp-site-2` (Red theme)
   - etc.
3. Each new site references THIS repo's CDN URLs

---

### **Option B: Rename Repository to "rtp-core"**

**Steps:**
1. Go to: https://github.com/poprtp88/TEST-RTP-BARU-2/settings
2. Scroll to "Repository name"
3. Change to: `rtp-core`
4. Click "Rename"

**New URLs will be:**
```
https://poprtp88.github.io/rtp-core/
```

**Then update all your files:**
- Replace `TEST-RTP-BARU-2` with `rtp-core`

---

## 🌐 CREATING ADDITIONAL WEBSITES

When you want to create your 2nd, 3rd... 10th website:

### **Step 1: Create New Repository**
```
Repository name: poprtp-site-2
Visibility: Public
```

### **Step 2: Create Files**

**index.html:**
```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <title>POP RTP Site 2</title>
    <link rel="stylesheet" href="styles.css">
    
    <!-- CDN Assets -->
    <link rel="icon" href="https://poprtp88.github.io/TEST-RTP-BARU-2/asset/favicon/favicon.jpg">
</head>
<body>
    <!-- Banners from CDN -->
    <img src="https://poprtp88.github.io/TEST-RTP-BARU-2/banner/1%20(1).jpg">
    
    <!-- Scripts from CDN -->
    <script src="https://poprtp88.github.io/TEST-RTP-BARU-2/game-data.js"></script>
    <script src="https://poprtp88.github.io/TEST-RTP-BARU-2/provider_image_lists.js"></script>
    <script src="https://poprtp88.github.io/TEST-RTP-BARU-2/game_popularity.js"></script>
    <script src="https://poprtp88.github.io/TEST-RTP-BARU-2/script.js"></script>
</body>
</html>
```

**styles.css:**
```css
/* Custom design for Site 2 - Red Theme */
:root {
    --accent-cyan: #ff0055;
    --accent-green: #ff6600;
}
```

---

## ✅ QUICK CHECKLIST

### **Immediate Actions:**
- [ ] Enable GitHub Pages for TEST-RTP-BARU-2
- [ ] Wait for deployment (2-5 minutes)
- [ ] Test CDN URLs load
- [ ] Update index.html (yourwebsite.com → poprtp.com)
- [ ] Update sitemap.xml (yourwebsite.com → poprtp.com)
- [ ] Update robots.txt (yourwebsite.com → poprtp.com)
- [ ] Add CDN config to script.js
- [ ] Update image paths in script.js
- [ ] Update banner sources in index.html
- [ ] Commit and push changes
- [ ] Test website loads correctly
- [ ] Verify CDN assets load
- [ ] Check console for errors

### **SEO Actions:**
- [ ] Update CNAME file with: poprtp.com
- [ ] Submit to Google Search Console
- [ ] Verify ownership
- [ ] Submit sitemap: https://poprtp.com/sitemap.xml
- [ ] Request indexing

---

## 🐛 TROUBLESHOOTING

### **Problem: CDN URLs return 404**

**Solution:**
1. Verify GitHub Pages is enabled
2. Wait 5-10 minutes after enabling
3. Check branch is set to `main`
4. Verify files exist in repository

### **Problem: Images don't load**

**Solution:**
1. Check CDN_PATHS in script.js
2. Verify image paths: `${CDN_PATHS.images}/${provider}/${imageName}`
3. Test direct URL in browser
4. Check for typos in provider names

### **Problem: Website doesn't show on poprtp.com**

**Solution:**
1. Check CNAME file contains: `poprtp.com`
2. Verify domain DNS points to GitHub Pages
3. Wait 24-48 hours for DNS propagation
4. Check GitHub Pages settings shows your domain

---

## 📞 SUMMARY

### **Your Setup:**
- ✅ **Core Repo:** https://github.com/poprtp88/TEST-RTP-BARU-2
- ✅ **CDN Base:** https://poprtp88.github.io/TEST-RTP-BARU-2/
- ✅ **Website:** https://poprtp.com/
- ✅ **GitHub User:** poprtp88

### **Files to Update:**
1. ✅ index.html (SEO URLs + banner sources)
2. ✅ sitemap.xml (domain URLs)
3. ✅ robots.txt (domain URLs)
4. ✅ script.js (CDN configuration)

### **Next Steps:**
1. Follow Phase 1-5 above
2. Test everything works
3. Submit to Google Search Console
4. Create additional sites as needed!

---

**Implementation Date:** December 10, 2025  
**Your Domain:** poprtp.com  
**Your GitHub:** poprtp88  
**Core Repository:** TEST-RTP-BARU-2  
**Status:** Ready to configure! 🚀

