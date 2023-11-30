let product_status = "all"

document.addEventListener("DOMContentLoaded", function () {
  renderProductList(page = 1, product_status = product_status)
  var modal = document.getElementById('myModal');
  window.onclick = function (event) {
    if (event.target == modal) {
      modal.style.display = "none";
    }
  }
})


// load product list
function renderProductList(page = 1, product_status = 'all') {
  let url = `/api/products?page=${page}&available=${product_status}`;

  fetch(url)
    .then(response => {
      return response.json()
    })
    .then(data => {
      const container = document.querySelector("#products-container");

      // clear item
      while (container.firstChild) {
        container.removeChild(container.lastChild)
      }

      renderPostsCallback(
        pages_total = data.pagination_meta.total_page,
        current_page = data.pagination_meta.current_page,
        has_previous = data.pagination_meta.has_prev,
        has_next = data.pagination_meta.has_next
      )

      // render item
      data["data"].forEach(item => {
        container.innerHTML += `
          <div class="card" id="produk-${item.id_produk}">
            <img class="product-img"
              src="https://user-images.githubusercontent.com/2351721/31314483-7611c488-ac0e-11e7-97d1-3cfc1c79610e.png">
            <div class="detail">
              <h3 class="nama_produk" style="margin-top: 0;">${item.nama_produk}</h3>
              <p class="detail-item harga">Harga: ${item.harga}</p>
              <p class="detail-item kategori">Kategori: ${item.kategori.nama_kategori}</p>
              <p class="detail-item status">Status: ${item.status.nama_status}</p>
            </div>
            <div class="card-action">
              <button class="card-action-button" onclick="openModal('edit', ${item.id_produk})">
                <img src="/static/images/pencils.png">
              </button>
              <button class="card-action-button" onclick="openModal('delete', ${item.id_produk})">
                <img src="/static/images/delete.png">
              </button>
            </div>
          </div>
          `
      })
    })
}

function renderPostsCallback(pages_total = 1, current_page = 1, has_previous = false, has_next = false) {
  /* control frontend pagination */
  let max = 5
  if (pages_total < 5) {
    max = pages_total
  }
  let max_left = 2
  if (current_page < 3) {
    max_left = current_page - 1
  }

  let max_right = max - 1 - max_left
  if (pages_total - current_page < 3) {
    max_right = pages_total - current_page
    max_left = max - 1 - max_right
  }

  const pagination_containers = document.querySelectorAll(".pagination")
  pagination_containers.forEach(item => {
    // clear
    while (item.firstChild) {
      item.removeChild(item.lastChild)
    }

    if (has_previous) {
      item.innerHTML += `
              <button class="page-item page-link" data-page="${current_page - 1}" onclick="onPagination(this)">Previous</button>
          `
      for (let i = current_page - max_left; i < current_page; i++) {
        item.innerHTML += `
                  <button class="page-item page-link" data-page="${i}" onclick="onPagination(this)">${i}</button>
              `
      }
    } else {
      // item.innerHTML += `
      //     <button class="page-item page-link inactive" data-page="prev" disabled>Previous</button>
      // `
    }

    item.innerHTML += `
          <button class="page-item page-link active" data-page="${current_page}" onclick="onPagination(this)">${current_page}</button>
      `

    if (has_next) {
      for (let i = current_page + 1; i < current_page + max_right + 1; i++) {
        item.innerHTML += `
                  <button class="page-item page-link" data-page="${i}" onclick="onPagination(this)">${i}</button>
              `
      }
      item.innerHTML += `
              <button class="page-item page-link" data-page="${current_page + 1}" onclick="onPagination(this)">Next</button>
          `
    } else {
      // item.innerHTML += `
      //     <button class="page-item page-link inactive" data-page="next" disabled>Next</button>
      // `
    }
  })
}

function onPagination(t) {
  renderProductList(page = parseInt(t.getAttribute("data-page"), product_status = product_status))
}

function onOptionChanged() {
  var selectedOption = document.getElementById("status").value;
  product_status = selectedOption
  renderProductList(page = 1, product_status = product_status)
}

function changeOption(otp) {
  product_status = otp
  document.getElementById("status").value = otp
}