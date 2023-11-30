document.addEventListener("DOMContentLoaded", function () {
})

function openModal(context, product_id = null) {
  var modal = document.getElementById('myModal');
  if (context == "add") {
    modalAdd()
  } else if (context == "edit") {
    modalEdit(product_id)
  }
  modal.style.display = "block";
}

function modalAdd() {
  modal_content = document.getElementById("modal-content");
  modal_content += `
    <div>
      <h3>Tambahkan Produk</h3>
      <form>
        <label for="nama_produk">Nama Produk:</label>
        <input type="text" id="nama_produk" name="nama_produk" required>

        <label for="harga">Harga:</label>
        <input type="text" id="harga" name="harga" required>

        <label for="kategori">Kategori:</label>
        <select id="kategori" name="kategori" required>
          <option value="">Pilih Kategori</option>
          <option value="electronics">Electronics</option>
          <option value="fashion">Fashion</option>
          <option value="food">Food</option>
        </select>

        <label for="status">Status:</label>
        <select id="status" name="status" required>
          <option value="">Pilih Status</option>
          <option value="dijual">Bisa Dijual</option>
          <option value="tidak_dijual">Tidak Bisa Dijual</option>
        </select>

        <button type="submit">Submit</button>
      </form>
    </div>

  `
}

function modalEdit(product_id) {

}

function closeModal() {
  var modal = document.getElementById('myModal');
  modal.style.display = "none";
}