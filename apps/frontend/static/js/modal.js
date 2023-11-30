document.addEventListener("DOMContentLoaded", function () {
})

async function openModal(context, product_id = null) {
  const modal = document.getElementById('myModal');
  const modal_content = document.querySelector(".modal-inner-content");
  // clear all child
  while (modal_content.firstChild) {
    modal_content.removeChild(modal_content.lastChild)
  }

  if (context === "delete") {
    modal_content.innerHTML = `
      <p>Apakah anda yakin ingin menghapus produk?</p>
      <button onclick="modalDeleteProduct(${product_id})">Hapus</button>
    `
  } else if (context === "add" || context === "edit") {
    const product_state = {
      id_produk: null,
      nama_produk: null,
      harga: null,
      id_kategori: null,
      id_status: null
    }
    if (context === "edit") {
      const product = await getProduct(product_id)
      product_state.id_produk = product.id_produk
      product_state.nama_produk = product.nama_produk
      product_state.harga = product.harga
      product_state.id_kategori = product.kategori.id_kategori
      product_state.id_status = product.status.id_status
      console.log(product_state)
    }

    // statuses
    var statuses_elm = ''
    const statuses = await getStatuses()
    statuses.forEach(item => {
      console.log(item)
      statuses_elm += `<option value="${item.id_status}" ${product_state.id_status === item.id_status ? 'selected' : ''}>${item.nama_status}</option>`
    })

    // categories
    var categories_elm = ''
    const categories = await getCategories()
    categories.forEach(item => {
      categories_elm += `<option value="${item.id_kategori}" ${product_state.id_kategori === item.id_kategori ? 'selected' : ''}>${item.nama_kategori}</option>`
    })

    let nama_product_value = ''
    if (product_state.nama_produk != null) {
      nama_product_value = product_state.nama_produk
    }

    let harga_value = ""
    if (product_state.harga != null) {
      harga_value = product_state.harga
    }

    modal_content.innerHTML += `
    <div>
      <h3>${context === "add" ? "Tambahkan Produk" : "Edit Produk"}</h3>
      <form>
        <p style="display: none" id="modalProductId">${product_state.id_produk}</p>
        <label for="nama_produk">Nama Produk:</label>
        <input type="text" id="nama_produk" name="nama_produk" value="${nama_product_value}" required>

        <label for="harga">Harga:</label>
        <input type="number" id="harga" name="harga" value="${harga_value}" required>

        <label for="kategori">Kategori:</label>
        <select id="kategori" name="kategori" required>
          ${categories_elm}
        </select>

        <label for="status">Status:</label>
        <select id="status" name="status" required>
          ${statuses_elm}
        </select>

      </form>
      <button
        onclick="${context === "add" ? "modalAddNewProduct()" : "modalPatchProduct()"}"
      >
        ${context === "add" ? "Tambahkan" : "Simpan"}
      </button>
    </div>
    `
  }
  modal.style.display = "block";
}

function closeModal() {
  var modal = document.getElementById('myModal');
  modal.style.display = "none";
}

async function modalAddNewProduct() {
  const modal_content = document.querySelector(".modal-inner-content");
  const payload = {
    nama_produk: modal_content.querySelector("#nama_produk").value,
    harga: modal_content.querySelector("#harga").value,
    id_kategori: modal_content.querySelector("#kategori").value,
    id_status: modal_content.querySelector("#status").value
  }
  if (payload.nama_produk === "" || payload.harga === "") {
    alert("nama produk dan harga tidak boleh kosong")
    closeModal()
    while (modal_content.firstChild) {
      modal_content.removeChild(modal_content.lastChild)
    }
    return
  }
  const data = await addNewProduct(payload)

  closeModal()
  // clear all child
  while (modal_content.firstChild) {
    modal_content.removeChild(modal_content.lastChild)
  }

  modalFinishCallback('add')
}

async function modalPatchProduct() {
  const modal_content = document.querySelector(".modal-inner-content");
  const product_id = modal_content.querySelector("#modalProductId").innerHTML
  const raw_payload = {
    nama_produk: modal_content.querySelector("#nama_produk").value,
    harga: modal_content.querySelector("#harga").value,
    id_kategori: modal_content.querySelector("#kategori").value,
    id_status: modal_content.querySelector("#status").value
  }
  if (raw_payload.nama_produk === "" || raw_payload.harga === "") {
    alert("nama produk dan harga tidak boleh kosong")
    closeModal()
    while (modal_content.firstChild) {
      modal_content.removeChild(modal_content.lastChild)
    }
    return
  }
  const payload = {}
  for (let key in raw_payload) {
    if (raw_payload[key] !== null) {
      payload[key] = raw_payload[key]
    }
  }
  const data = await patchProduct(payload, product_id)

  closeModal()
  // clear all child
  while (modal_content.firstChild) {
    modal_content.removeChild(modal_content.lastChild)
  }
  modalFinishCallback('edit', data)
}

async function modalDeleteProduct(product_id) {
  const modal_content = document.querySelector(".modal-inner-content");
  try {
    await deleteProduct(product_id)
  } catch (error) {
    alert("gagal menghapus produk")
  }
  closeModal()
  while (modal_content.firstChild) {
    modal_content.removeChild(modal_content.lastChild)
  }
  modalFinishCallback('delete')
}

function modalFinishCallback(context, data = {}) {
  if (context === "add" || context === "delete") {
    changeOption("all")
    renderProductList(page = 1, product_status = product_status)
  } else if (context === "edit") {
    const selected_product = document.getElementById(`produk-${data.id_produk}`)
    selected_product.querySelector(".nama_produk").innerHTML = data.nama_produk
    selected_product.querySelector(".harga").innerHTML = `Harga: ${data.harga}`
    selected_product.querySelector(".kategori").innerHTML = `Kategori: ${data.kategori.nama_kategori}`
    selected_product.querySelector(".status").innerHTML = `Status: ${data.status.nama_status}`
  }
}