// mainList.html 부분
const requestLoc = new XMLHttpRequest();

const onClickLocation = (location) => {
  requestLoc.open("POST", "/locations/", true);
  requestLoc.setRequestHeader(
    "Content-Type",
    "application/x-www-form-urlencoded"
  );
  requestLoc.send(JSON.stringify({ location: location }));
};

requestLoc.onreadystatechange = () => {
  if (requestLoc.readyState === XMLHttpRequest.DONE) {
    if (requestLoc.status < 400) {
      //  views.py/locations 에서 보내준 data 화면에 뿌리기
    }
  }
};

// 멍카페, 멍숙소, 멍놀자 세부선택 ajax 처리
const requestCate = new XMLHttpRequest();
const onClickCate = (cate) => {
  // 질문!! -> 눌렀을 때 서버로 데이터 가져와서 뿌려주는 게 아닌데 이 부분 필요? 간소화?
  requestCate.open("POST", "/cates/", true);
  requestCate.setRequestHeader(
    "Content-Type",
    "application/x-www-form-urlencoded"
  );
  requestCate.send(JSON.stringify({ cate: cate }));
};

requestCate.onreadystatechange = () => {
  if (requestCate.readyState === XMLHttpRequest.DONE) {
    if (requestCate.status < 400) {
      const { cate } = JSON.parse(requestCate.response);
      const detailBox = document.querySelector("#left-detail");

      if (cate == "카페") {
        detailBox.innerHTML = `<form action="">
  <div>
    <input type="radio" name="cafe-detail" value="dogs-only" />애견 전용
  </div>
  <div>
    <input type="radio" name="cafe-detail" value="dogs-can" />애견 동반
  </div>
</form>`;
      } else if (cate == "숙소") {
        detailBox.innerHTML = `<form action="">
  <div>
    <input type="radio" name="accomo-detail" value="hotel" />호텔
  </div>
  <div>
    <input type="radio" name="accomo-detail" value="motel" />모텔
  </div>
  <div>
    <input type="radio" name="accomo-detail" value="resort" />리조트
  </div>
  <div>
    <input type="radio" name="accomo-detail" value="pension" />펜션
  </div>
</form>`;
      } else if (cate == "장소") {
        detailBox.innerHTML = `<form action="">
  <div>
    <input type="radio" name="place-detail" value="park" />공원
  </div>
  <div>
    <input type="radio" name="place-detail" value="pool" />수영장
  </div>
  <div>
    <input type="radio" name="place-detail" value="beach" />해변
  </div>
</form>`;
      }
    }
  }
};
