const modal = document.getElementById("myModal");
const openModalBtn = document.getElementById("exitModal");
const closeModal = document.getElementsByClassName("close")[0];

openModalBtn.onclick = function () {
    modal.style.display = "block";
};
closeModal.onclick = function () {
    modal.style.display = "none";
};

window.onclick = function (event) {
    if (event.target === modal) {
        modal.style.display = "none";
    }
};

let elementError = `        
        <div class="messages error">
            <p>
                Erro não e possivel sacar o valor! - Tente novamente
            </p>    
        </div>
    `;
const withdraw = document.getElementById("withdraw");
withdraw.onclick = function () {
    const drawnError = document.getElementById("drawnError");
    drawnError.innerHTML = elementError;
};

const valueSize = document.getElementById("valueSize");
valueSize.innerHTML = Math.round((valueSize.innerText / 100) * 33.33 * 30);
