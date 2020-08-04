import { getParkList, getEmployeeList, retrieveAttraction, getParkAttractions } from "./services.js"



const drawPark = () => { }


const drawEmployees = () => {} 



// get all the attractions in a park, display the % make up of attractions by attraction type.
export const drawAttractionTypes = (parkId) => {
  let parks = [];
  getParkAttractions().then((attractions) => {
    const filterByPark = attractions.filter((attraction) => attraction.park_id === parkId);
    parks.push(filterByPark);
    const attractionIds = filterByPark.map((attraction) => attraction.attraction_id);
    attractionIds.forEach((id) => {
      retrieveAttraction(id).then((response) => {
        console.log(response);
      });
    });
  });
};

drawAttractionTypes(1);
