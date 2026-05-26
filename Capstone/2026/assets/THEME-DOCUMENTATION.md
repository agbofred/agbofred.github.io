# Custom Color Theme Documentation

## Overview
This custom color theme is inspired by Professor Fred Agbo's professional website ([fredagbo.com](https://fredagbo.com/)) and designed specifically for the CS 481W/482 Senior Capstone Project course materials.

## Design Philosophy
The theme combines modern educational technology aesthetics with professional polish, reflecting:
- **Academic Excellence**: Deep professional blues convey trust and expertise
- **Innovation Focus**: Vibrant orange accents represent creativity and energy
- **Educational Technology**: Teal secondary colors symbolize growth and learning
- **Accessibility**: High contrast ratios and responsive design ensure inclusivity

## Color Palette

### Primary Colors (Professional Blues)
- `--primary-dark: #0A4C6D` - Deep ocean blue for headings and emphasis
- `--primary-main: #1E5A7D` - Main brand color for primary elements
- `--primary-light: #2C6B8E` - Lighter shade for interactive elements
- `--primary-lighter: #4A8FAF` - Subtle accents and hover states

### Accent Colors (Vibrant Tech Orange)
- `--accent-main: #FF6B35` - Bold orange for calls-to-action
- `--accent-dark: #E65A25` - Deeper shade for active states
- `--accent-light: #FF8558` - Lighter variant for highlights

### Secondary Colors (Educational Teal)
- `--secondary-main: #16A085` - Teal for success and growth indicators
- `--secondary-dark: #138D75` - Darker teal for emphasis
- `--secondary-light: #1ABC9C` - Light teal for subtle accents

### Text Colors
- `--text-primary: #2C3E50` - Main body text (dark slate)
- `--text-secondary: #5D6D7E` - Secondary text (medium gray)
- `--text-light: #7F8C8D` - Tertiary text (light gray)
- `--text-white: #FFFFFF` - White text for dark backgrounds

### Background Colors
- `--bg-primary: #FFFFFF` - Main content background
- `--bg-secondary: #F8F9FA` - Subtle gray for sections
- `--bg-tertiary: #ECF0F1` - Lighter gray for nested elements
- `--bg-dark: #34495E` - Dark background for code blocks

## Key Features

### 1. Modern Gradient Accents
- Header borders use gradient transitions from accent orange to teal
- Buttons feature gradient backgrounds for visual depth
- Welcome section has a sophisticated gradient overlay

### 2. Enhanced Typography
- Clean sans-serif font stack for optimal readability
- Hierarchical heading styles with visual indicators
- Color-coded headings for quick content scanning

### 3. Interactive Elements
- Smooth transitions on all interactive components
- Hover effects with subtle transforms and shadows
- Custom-styled links with animated underlines

### 4. Accessibility Features
- WCAG 2.1 AA compliant color contrasts
- Focus indicators for keyboard navigation
- Reduced motion support for users with vestibular disorders
- High contrast mode support

### 5. Responsive Design
- Mobile-first approach with breakpoints
- Fluid typography and spacing
- Touch-friendly interactive elements

### 6. Visual Hierarchy
- Left-border accents on headings (gradient bars)
- Section cards with hover effects
- Color-coded list items with custom bullets
- Styled tables with gradient headers

## Usage

### Automatic Application
The theme is automatically applied through:
1. `_quarto.yml` configuration file
2. YAML frontmatter in markdown files
3. Direct CSS links in HTML files

### Manual Override
To customize specific elements, add inline styles or create additional CSS files that load after `custom-theme.css`.

## File Structure
```
2026/
├── assets/
│   ├── custom-theme.css         # Main theme file
│   └── THEME-DOCUMENTATION.md   # This file
├── _quarto.yml                  # Quarto configuration
├── index.md                     # Homepage source
├── syllabi.md                   # Syllabus source
├── index.html                   # Rendered homepage
└── syllabi.html                 # Rendered syllabus
```

## Credits
**Designer/Developer**: Professor Fred Agbo, PhD  
**Inspiration**: fredagbo.com  
**Date**: May 2026  
**Version**: 1.0

---

For questions or customization requests, contact: fjagbo@willamette.edu
