async function getProduct(product_id) {
    try {
        const response = await fetch(`/api/products/${product_id}`);
        if (!response.ok) {
            throw new Error('resp not ok');
        }
        const data = await response.json();
        return data.data;
    } catch (error) {
        console.error('error fetching product:', error);
    }
}

async function getStatuses() {
    try {
        const response = await fetch("/api/statuses?show_all=true");
        if (!response.ok) {
            throw new Error('resp not ok');
        }
        const data = await response.json();
        return data.data;
    } catch (error) {
        console.error('error fetching statuses:', error);
    }
}

async function getCategories() {
    try {
        const response = await fetch("/api/categories?show_all=true");
        if (!response.ok) {
            throw new Error('resp not ok');
        }
        const data = await response.json();
        return data.data;
    } catch (error) {
        console.error('error fetching categories:', error);
    }
}

async function addNewProduct(payload) {
    try {
        const response = await fetch("/api/products", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
        });
        if (!response.ok) {
            throw new Error('resp not ok');
        }
        const data = await response.json();
        return data.data;
    } catch (error) {
        console.error('error adding new product:', error);
    }
}

async function patchProduct(payload, product_id) {
    try {
        const response = await fetch(`/api/products/${product_id}`, {
            method: 'PATCH',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
        });
        if (!response.ok) {
            throw new Error('resp not ok');
        }
        const data = await response.json();
        return data.data;
    } catch (error) {
        console.error('error adding editing a product:', error);
    }
}

async function deleteProduct(product_id) {
    try {
        const response = await fetch(`/api/products/${product_id}`, {
            method: 'DELETE',
        });
        if (!response.ok) {
            throw new Error('resp not ok');
        }
    } catch (error) {
        console.error('error adding editing a product:', error);
    }
}



