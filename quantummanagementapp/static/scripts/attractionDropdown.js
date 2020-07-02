const parkSelect = document.getElementById("parks");
const id = parkSelect.getAttribute("data-park-id");
const parks = document.getElementById("parks");
const attractionOptionNodes = document.querySelectorAll(".attraction_option_dropdown");
const attractionsSelect = document.getElementById("employee_attraction");
const parkOptionNodes = document.querySelectorAll(".park_options_dropdown");

// attractionOptions = All option nodes in the dropdown in an array
// filteredAttractionOptions = filtered out option nodes in an array, of matching attraction Id and park id.
// attractionsSelect = grab reference to the select drop down
// clear the innerHTMl by setting it to an empty string
// Iterate the filtered options, grab the string template from outerHTML attribute, reset the innerHTML/ dropdown list with string templates.

window.onload = () => {
  const attractionOptions = Array.from(attractionOptionNodes);
  const currentPark = parks.value;
  const filteredAttractionOptions = attractionOptions.filter((option) => currentPark === option.dataset.parkId);
  attractionsSelect.innerHTML = "";
  filteredAttractionOptions.forEach((option) => {
    const optionStringHTML = option.outerHTML;
    attractionsSelect.innerHTML += optionStringHTML;
  });
};

function filterAttractionDropdown(selectHTMLElement) {
  selectHTMLElement.addEventListener("change", (e) => {
    const parkId = e.target.value;
    const attractionOptions = Array.from(attractionOptionNodes);
    const filteredAttractionOptions = attractionOptions.filter((option) => parkId === option.dataset.parkId);
    attractionsSelect.innerHTML = "";
    filteredAttractionOptions.forEach((option) => {
      const optionStringHTML = option.outerHTML;
      attractionsSelect.innerHTML += optionStringHTML;
    });
  });
}


filterAttractionDropdown(attractionsSelect);
