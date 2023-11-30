var modal = document.getElementById('myModal');
var open_mdl_btn = document.getElementById("openModalBtn");
var close_mdl_btn = document.getElementById("closeModalBtn");

window.onclick = function (event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

function openModal(content) {
  modal.style.display = "block";
}

function closeModal() {
  modal.style.display = "none";
}