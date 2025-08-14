/**
 * Image Handler for TueLinh Real Estate
 * Handles image loading errors and provides fallback mechanisms
 */

// Global configuration for image placeholders
const IMAGE_CONFIG = {
    placeholders: [
        '/static/images/property-placeholder.svg',
        '/static/images/property-placeholder.jpg',
        'data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjMwMCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8cmVjdCB3aWR0aD0iNDAwIiBoZWlnaHQ9IjMwMCIgZmlsbD0iI2Y4ZjlmYSIvPgogIDx0ZXh0IHg9IjUwJSIgeT0iNTAlIiBmb250LWZhbWlseT0iQXJpYWwiIGZvbnQtc2l6ZT0iMTgiIGZpbGw9IiM2Yzc1N2QiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGR5PSIuM2VtIj5Lb25nIGPDsyBoaW5oIGFuaDwvdGV4dD4KPC9zdmc+'
    ],
    defaultStyles: {
        backgroundColor: '#f8f9fa',
        border: '1px solid #dee2e6',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center'
    }
};

/**
 * Handle image loading errors with fallback mechanism
 * @param {HTMLImageElement} img - The image element that failed to load
 */
function handleImageError(img) {
    if (!img || !img.onerror) return;
    
    // Prevent infinite loop
    img.onerror = null;
    
    // Get current src to determine next fallback
    const currentSrc = img.src;
    let nextPlaceholder = null;
    
    // Find next placeholder in sequence
    for (let i = 0; i < IMAGE_CONFIG.placeholders.length; i++) {
        const placeholder = IMAGE_CONFIG.placeholders[i];
        if (currentSrc.includes(placeholder.split('/').pop()) || currentSrc === placeholder) {
            // Current is this placeholder, try next one
            if (i < IMAGE_CONFIG.placeholders.length - 1) {
                nextPlaceholder = IMAGE_CONFIG.placeholders[i + 1];
            }
            break;
        }
    }
    
    // If no specific next placeholder found, use first one
    if (!nextPlaceholder) {
        nextPlaceholder = IMAGE_CONFIG.placeholders[0];
    }
    
    // Set new source
    img.src = nextPlaceholder;
    img.alt = 'Không có hình ảnh';
    
    // Apply default styles
    Object.assign(img.style, IMAGE_CONFIG.defaultStyles);
    
    // Add error class for additional styling
    img.classList.add('image-error');
    
    console.log('Image fallback applied:', nextPlaceholder);
}

/**
 * Preload placeholder images for better performance
 */
function preloadPlaceholderImages() {
    IMAGE_CONFIG.placeholders.forEach(src => {
        if (src.startsWith('data:')) return; // Skip base64 images
        
        const img = new Image();
        img.onload = () => console.log('Placeholder preloaded:', src);
        img.onerror = () => console.warn('Failed to preload placeholder:', src);
        img.src = src;
    });
}

/**
 * Initialize lazy loading for images
 */
function initLazyLoading() {
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    if (img.dataset.src) {
                        img.src = img.dataset.src;
                        img.removeAttribute('data-src');
                        imageObserver.unobserve(img);
                    }
                }
            });
        });
        
        // Observe all images with data-src attribute
        document.querySelectorAll('img[data-src]').forEach(img => {
            imageObserver.observe(img);
        });
    }
}

/**
 * Add loading animation to images
 */
function addImageLoadingEffects() {
    const images = document.querySelectorAll('img[loading="lazy"]');
    
    images.forEach(img => {
        // Add loading class initially
        img.classList.add('image-loading');
        
        // Remove loading class when image loads
        img.onload = function() {
            this.classList.remove('image-loading');
            this.classList.add('image-loaded');
        };
        
        // Handle error
        if (!img.onerror) {
            img.onerror = function() {
                handleImageError(this);
            };
        }
    });
}

/**
 * Main image gallery functionality for property detail pages
 */
function initImageGallery() {
    const mainImage = document.querySelector('.main-image');
    const thumbnails = document.querySelectorAll('.thumbnail');
    
    if (!mainImage || !thumbnails.length) return;
    
    thumbnails.forEach(thumbnail => {
        thumbnail.addEventListener('click', function() {
            // Remove active class from all thumbnails
            thumbnails.forEach(t => t.classList.remove('active'));
            
            // Add active class to clicked thumbnail
            this.classList.add('active');
            
            // Change main image
            mainImage.src = this.src;
            mainImage.alt = this.alt;
        });
    });
}

/**
 * Initialize all image handling features
 */
function initImageHandler() {
    // Preload placeholders
    preloadPlaceholderImages();
    
    // Initialize lazy loading
    initLazyLoading();
    
    // Add loading effects
    addImageLoadingEffects();
    
    // Initialize gallery
    initImageGallery();
    
    console.log('Image handler initialized');
}

// Initialize when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initImageHandler);
} else {
    initImageHandler();
}

// Export functions for global use
window.handleImageError = handleImageError;
window.changeMainImage = function(src) {
    const mainImage = document.querySelector('.main-image');
    if (mainImage) {
        mainImage.src = src;
    }
};
