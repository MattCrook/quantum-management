const parkSelect = document.getElementById("parks");
const attractionsSelect = document.getElementById("employee_attraction");
const parkDropdownOptions = document.querySelectorAll(".park_options_dropdown");
// get the value of the park selected
// do a check if the value in join table
// then poplulate dropdown with all attrations in that park_id

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




parkSelect.addEventListener("click", (e) => {
    const parkValue = e.target.value;
})

attractionsSelect.addEventListener("click", (e) => {
    const attractionValue = e.target.id;
})
