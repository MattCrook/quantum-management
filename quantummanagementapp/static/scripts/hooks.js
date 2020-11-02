const useVisitors = () => {
    let visitors = [];
      return [
          () => visitors.slice(),
          (newVisitor) => (visitors = newVisitor.splice(0))
      ];
  };


  const useAttractions = () => {
    let attractions = [];
      return [
          () => attractions.slice(),
          (newAttractions) => (attractions = newAttractions.splice(0))
      ];
  };

  const useAttractionVisitorsData = () => {
    let attractionVisitorsData = [];
      return [
          () => attractionVisitorsData.slice(),
          (newAttractionVisitorsData) => (attractionVisitorsData = newAttractionVisitorsData.splice(0))
      ];
  };

export {useVisitors, useAttractions, useAttractionVisitorsData}
