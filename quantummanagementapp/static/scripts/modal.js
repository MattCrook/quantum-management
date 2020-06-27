

const createTypeLink = document.getElementById("modal-1");

MicroModal.init({
    onShow: modal => console.info(`${modal.id} is shown`),
    onClose: modal => console.info(`${modal.id} is hidden`),
    openTrigger: 'data-micromodal-trigger',
    closeTrigger: 'data-micromodal-close', 
    openClass: 'is-open',
    disableScroll: true,
    disableFocus: false,
    awaitOpenAnimation: true,
    awaitCloseAnimation: false,
    debugMode: true
});





// const infoDialog = document.querySelector(".infoDialog");
// const message = document.querySelector(".infoDialog__message");
// const closeDialog = document.querySelector(".closeDialog");

// document.querySelector(".books").addEventListener("click", (e) => {
//   if (e.target.id.startsWith("detail")) {
//     const id = e.target.id.split("--")[1];
//     message.innerText = `You have selected book ${id}`;
//     infoDialog.show();
//   }
// });

// closeDialog.addEventListener("click", (e) => infoDialog.close());

// window.addEventListener("keyup", (e) => {
//   if (e.keyCode === 27) {
//     infoDialog.close();
//   }
// });
