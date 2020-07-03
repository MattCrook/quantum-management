const remoteURL = "http://localhost:8000";

const createTypeLink = document.getElementById("modal-1");
const deleteAttractionLink = document.getElementById("modal__btn-primary2");

MicroModal.init({
  openTrigger: "data-micromodal-trigger",
  closeTrigger: "data-micromodal-close",
  openClass: "is-open",
  disableScroll: true,
  disableFocus: false,
  awaitOpenAnimation: true,
  awaitCloseAnimation: false,
  debugMode: true,
});


// Pop Up for DELETE attraction option.
const attractions = document.getElementById("attractions");
const options = document.querySelectorAll(".attraction_delete_dropdown");
const attractionNodes = Array.prototype.slice.call(options);

attractions.addEventListener("change", (e) => {
    const attractionId = e.target.value;
    const name = attractions.selectedOptions[0].innerHTML;
      deleteAttractionLink.addEventListener("click", () => {
        window.confirm(`Are you sure you want to delete ${name}?`);
      });
    });
