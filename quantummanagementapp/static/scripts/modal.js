const remoteURL = "http://localhost:8000";

const createTypeLink = document.getElementById("modal-1");

MicroModal.init({
    openTrigger: 'data-micromodal-trigger',
    closeTrigger: 'data-micromodal-close',
    openClass: 'is-open',
    disableScroll: true,
    disableFocus: false,
    awaitOpenAnimation: true,
    awaitCloseAnimation: false,
    debugMode: true
});