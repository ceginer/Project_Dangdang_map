// medicalList에서 검색 눌렀을 때

const requestMedical = new XMLHttpRequest();
const onclickMedical = () => {
  requestMedical.open("POST", "/medicals/", true);
  requestMedical.setRequestHeader(
    "Content-Type",
    "application/x-www-form-urlencoded"
  );
  var location = document.getElementById("location");
  var loc = location.options[location.selectedIndex].text;
  var query = document.getElementById("query-loc").value;
  console.log(loc, query);
  requestMedical.send(JSON.stringify({ loc: loc, query: query }));
};

requestMedical.onreadystatechange = () => {
  if (requestMedical.readyState === XMLHttpRequest.DONE) {
    if (requestMedical.status <= 400) {
      const { list, query, loc, x, y } = JSON.parse(requestMedical.response);
      medical = JSON.parse(list);
      const ele = document.querySelector(".medical_list_container");
      ele.innerHTML = ``;
      for (var i = 0; i < 10; i++) {
        ele.innerHTML += `<div class="medical_item">
        <div class="medical_info">
          <div class="medical_name">${medical[i]["fields"]["name"]}</div>
          <div class="medical_address">${medical[i]["fields"]["address"]}</div>
          <div class="medical_phone">${medical[i]["fields"]["phone"]}</div>
          <div class="info_bottom">
            <a href="${medical[i]["fields"]["link"]}"><button class="find_location">위치찾기</button></a>
          </div>
        </div>
      </div>`;
      }
    }
  }
};
