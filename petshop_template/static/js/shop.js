// Generates HTML markup for each product card
function createProductCard(product) {
    return `
        <div class="col-md-4 mb-4">
            <div class="card h-100 shadow-sm">
                <img src="${product.image}" class="card-img-top" alt="${product.name}">
                <div class="card-body">
                    <h5 class="card-title fw-bold">${product.name}</h5>
                    <p class="card-text">${product.description}</p>
                    <div class="d-flex justify-content-between align-items-center">
                        <span class="h5 mb-0">$${product.price}</span>
                        <div>
                            <button class="btn btn-outline-dark btn-custom rounded-0 add-to-cart" 
                                    data-id="${product.id}">
                                <i class="bi bi-cart-plus me-2"></i>Add to Cart
                            </button>
                            <button class="btn btn-outline-dark btn-custom rounded-0 add-to-cart delete-product ms-2" 
                                    data-id="${product.id}">
                                <i class="bi bi-trash"></i>
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    `;
}

// Generates the shop page structure
export default function getShop() {
    return `
        <div class="container py-5" id="products">
            <h2 class="display-4 fw-bold mb-5 text-center">Products</h2>      
            <section class="mb-5">
                <h3 class="fw-bold mb-4">Dog Products</h3>
                <div class="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4" id="dog-products">
                    <div class="col-12 text-center">
                        <div class="spinner-border text-primary" role="status">
                            <span class="visually-hidden">Loading...</span>
                        </div>
                    </div>
                </div>
            </section>
            <section>
                <h3 class="fw-bold mb-4">Cat Products</h3>
                <div class="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4" id="cat-products">
                    <div class="col-12 text-center">
                        <div class="spinner-border text-primary" role="status">
                            <span class="visually-hidden">Loading...</span>
                        </div>
                    </div>
                </div>
            </section>
        </div>
    `;
}

// Initializes the shop component
export async function initShop() {
    const renderProducts = (containerId, category, products) => {
        const container = document.getElementById(containerId);
        if (container) {
            container.innerHTML = products
                .map(product => createProductCard(product))
                .join('');

            // Attach delete event listeners
            container.querySelectorAll('.delete-product').forEach(button => {
                button.addEventListener('click', async (event) => {
                    const productId = event.target.closest('button').dataset.id;
                    await deleteProduct(productId);
                });
            });
        }
    };

    try {
        // Fetch products from Django backend
        const response = await fetch('http://localhost:8000/api/products/');
        if (!response.ok) {
            throw new Error('Failed to fetch products');
        }
        const productsByCategory = await response.json();

        // Render both product categories
        renderProducts('dog-products', 'dog', productsByCategory.dog);
        renderProducts('cat-products', 'cat', productsByCategory.cat);
    } catch (error) {
        console.error('Error loading products:', error);
    }
}

async function deleteProduct(productId) {
    if (!productId) {
        console.error("Product ID is undefined. Check the data-id attribute on the button.");
        return;
    }

    if (!confirm("Are you sure you want to delete this product?")) return;

    try {
        const deleteUrl = `http://localhost:8000/api/products/${productId}/delete/`;
        console.log("Sending DELETE request to:", deleteUrl);

        const response = await fetch(deleteUrl, {
            method: "DELETE",
            headers: {
                "Content-Type": "application/json"
            },
            credentials: "include" // Include cookies in the request
        });

        if (!response.ok) {
            throw new Error("Failed to delete product");
        }

        console.log("Product deleted successfully. Refreshing product list...");
        alert("Product deleted successfully");
        initShop(); // Refresh product list
    } catch (error) {
        console.error("Error deleting product:", error);
        alert("Could not delete product. Try again.");
    }
}

// Initialize the shop when the DOM is fully loaded
document.addEventListener("DOMContentLoaded", function () {
    console.log("DOM fully loaded. Initializing shop...");
    initShop();
});