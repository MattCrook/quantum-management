const getParkList = async () => {
  try {
    const response = await fetch(`/api/parks`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
    });
    if (response.ok) {
      return await response.json();
    }
    throw new Error("Request Failed");
  } catch (err) {
    console.log(err);
  }
};

const getEmployeeList = async () => {
  try {
    const response = await fetch(`/api/employees`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
    });
    if (response.ok) {
      return await response.json();
    }
    throw new Error("Request Failed");
  } catch (err) {
    console.log(err);
  }
};

const retrieveAttraction = async (id) => {
  try {
    const response = await fetch(`/api/attractions/${id}`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
    });
    if (response.ok) {
      return await response.json();
    }
    throw new Error("Request Failed");
  } catch (err) {
    console.log(err);
  }
};

const getParkAttractions = async (parkId) => {
  try {
    const response = await fetch(`/api/park_attractions?park_id=${parkId}`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
    });
    if (response.ok) {
      return await response.json();
    }
    throw new Error("Request Failed");
  } catch (err) {
    console.log(err);
  }
};

const getAttractions = async (parkId) => {
  try {
    const response = await fetch(`/api/attractions?park_id=${parkId}`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
    });
    if (response.ok) {
      return await response.json();
    }
    throw new Error("Request Failed");
  } catch (err) {
    console.log(err);
  }
};

const getAttractionType = async (typeId) => {
  try {
    const response = await fetch(`/api/attraction_types/${typeId}`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
    });
    if (response.ok) {
      return await response.json();
    }
    throw new Error("Request Failed");
  } catch (err) {
    console.log(err);
  }
};

const getVisitorsList = async (parkId) => {
  try {
    const response = await fetch(`/api/visitors?park_id=${parkId}`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
    });
    if (response.ok) {
      return await response.json();
    }
    throw new Error("Request Failed");
  } catch (err) {
    console.log(err);
  }
};

const getAttractionWaitTimes = async (parkId) => {
  try {
    const response = await fetch(`/api/attraction_wait_times?park_id=${parkId}`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
    });
    if (response.ok) {
      return await response.json();
    }
    throw new Error("Request Failed");
  } catch (err) {
    console.log(err);
  }
};

const getAttractionVisitors = async (attractionId) => {
  try {
    const response = await fetch(`/api/attraction_visitors?attraction_id=${attractionId}`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
    });
    if (response.ok) {
      return await response.json();
    }
    throw new Error("Request Failed");
  } catch (err) {
    console.log(err);
  }
};

export {
  getParkList,
  getEmployeeList,
  retrieveAttraction,
  getParkAttractions,
  getAttractions,
  getAttractionType,
  getVisitorsList,
  getAttractionWaitTimes,
  getAttractionVisitors,
};
