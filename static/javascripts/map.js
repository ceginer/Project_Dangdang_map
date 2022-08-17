var mapContainer = document.getElementById("map"), // 지도를 표시할 div
  mapOption = {
    center: new kakao.maps.LatLng(x, y), // 지도의 중심좌표
    level: 3, // 지도의 확대 레벨
  };

// 지도를 생성합니다
var map = new kakao.maps.Map(mapContainer, mapOption);

var coords = new kakao.maps.LatLng(x, y);

var marker = new kakao.maps.Marker({
  map: map,
  position: coords,
});

var infowindow = new kakao.maps.InfoWindow({
  content: `<div style="width:150px;text-align:center;padding:6px 0;">${name}</div>`,
});
infowindow.open(map, marker);
