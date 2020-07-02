const parkSelect = document.getElementById("parks");
const id = parkSelect.getAttribute("data-park-id");

const park = document.getElementById("parks");
const attractionOptionNodes = document.querySelectorAll(".attraction_option_dropdown");

park.addEventListener("change", (e) => {
    const parkId = e.target.value;
    // All option nodes in the dropdown in an array
    const attractionOptions = Array.from(attractionOptionNodes);
    // filtered out option nodes in an array, of matching attraction Id and park id.
    const filteredAttractionOptions = attractionOptions.filter(option => parkId === option.dataset.parkId);
    console.log(filteredAttractionOptions)
    // grab reference to the select drop down
    const attractionsSelect = document.getElementById("employee_attraction");
    attractionsSelect.innerHTML = '';
    attractionsSelect.innerHTML += filteredAttractionOptions
})



















// function useParksDropdown() {
//   let park = parkSelect.value;
//   return [() => park, (filteredParks) => (park = filteredPark)];
// }
// const [park, setPark] = useParksDropdown();

// function useAttractionsDropdown() {
//   let attractions = attractionsSelect.value;
//   return [
//     () => attractions,
//     (filteredAttractions) => (attractions = filteredAttractions),
//   ];
// }
// const [attractions, setAttractions] = useAttractionsDropdown([]);

// parkSelect.addEventListener("click", (e) => {
//   const stateToChange = [...attractionsSelect];
//   console.log("stateToChange", stateToChange);
// console.log(e.target.value)
// const parkValue = e.target.value;

// stateToChange[e.target.id] = e.target.value;
// const filter = stateToChange.filter(attractions => attractions.value === ))
// console.log(filter)
//   setAttractions(stateToChange);
