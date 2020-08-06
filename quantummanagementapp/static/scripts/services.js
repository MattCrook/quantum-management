export async function getParkList() {
  try {
    const response = await fetch(`/api/parks`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
    });
    if (response.ok) {
      const jsonResponse = await response.json();
      return jsonResponse;
    }
    throw new Error("Request Failed");
  } catch (err) {
    console.log(err);
  }
}

export async function getEmployeeList() {
  try {
    const response = await fetch(`/api/employees`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
    });
    if (response.ok) {
      const jsonResponse = await response.json();
      return jsonResponse;
    }
    throw new Error("Request Failed");
  } catch (err) {
    console.log(err);
  }
}

export async function retrieveAttraction(id) {
  try {
    const response = await fetch(`/api/attractions/${id}`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
    });
    if (response.ok) {
      const jsonResponse = await response.json();
      return jsonResponse;
    }
    throw new Error("Request Failed");
  } catch (err) {
    console.log(err);
  }
}

export async function getParkAttractions(parkId) {
  try {
    const response = await fetch(`/api/park_attractions?park_id=${parkId}`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
    });
    if (response.ok) {
      const jsonResponse = await response.json();
      return jsonResponse;
    }
    throw new Error("Request Failed");
  } catch (err) {
    console.log(err);
  }
}

export async function getAttractionType(typeId) {
  try {
    const response = await fetch(`/api/attraction_types/${typeId}`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
    });
    if (response.ok) {
      const jsonResponse = await response.json();
      return jsonResponse;
    }
    throw new Error("Request Failed");
  } catch (err) {
    console.log(err);
  }
}
