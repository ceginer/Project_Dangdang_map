//home.html부분

const requestHomeLeft = new XMLHttpRequest(); //어디로 떠날까요? 부분
const onClickHome = (direction) => {
  requestHomeLeft.open("POST", "/btn_main/", true);
  requestHomeLeft.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
  requestHomeLeft.send(JSON.stringify({direction: direction}));
};

requestHomeLeft.onreadystatechange = () => {
  if (requestHomeLeft.readyState === XMLHttpRequest.DONE) {
    if (requestHomeLeft.status <= 400) {
      const {direction} = JSON.parse(requestHomeLeft.response); 
      let element = document.querySelector("#num"); 
      let count = Number(element.innerHTML); 
      
      if (direction == "left") {
        count -= -1;
        if (count == -1) {
          count = 2
        }
        else {
          count %= 2
        }
      }
      else {
        count += 1;
        count %= 3
      }

      element.innerHTML = `${count}`;
      
      if (count == 0) {
        const locationSet = document.querySelector(".shift-locations");
        locationSet.innerHTML = `<div class="home_location"><a href="/cities/서울">서울</a></div>
        <div class="home_location"><a href="/cities/경기">경기</a></div>
        <div class="home_location"><a href="/cities/인천">인천</a></div>
        <div class="home_location"><a href="/cities/강원">강원</a></div>
        <div class="home_location"><a href="/cities/충북">충북</a></div>
        <div class="home_location"><a href="/cities/충남">충남</a></div>`
        const page = document.querySelector(".page_dot");
        page.innerHTML ='<img src="/static/img/page_1.svg" alt="">'
      }
      else if (count == 1) {
        const locationSet = document.querySelector(".shift-locations");
        locationSet.innerHTML = `<div class="home_location"><a href="/cities/대전">대전</a></div>
        <div class="home_location"><a href="/cities/경북">경북</a></div>
        <div class="home_location"><a href="/cities/경남">경남</a></div>
        <div class="home_location"><a href="/cities/대구">대구</a></div>
        <div class="home_location"><a href="/cities/울산">울산</a></div>
        <div class="home_location"><a href="/cities/부산">부산</a></div>`
        const page = document.querySelector(".page_dot");
        page.innerHTML ='<img src="/static/img/page_2.svg" alt="">'
      }
      else {
        const locationSet = document.querySelector(".shift-locations");
        locationSet.innerHTML = `<div class="home_location"><a href="/cities/광주">광주</a></div>
        <div class="home_location"><a href="/cities/전북">전북</a></div>
        <div class="home_location"><a href="/cities/전남">전남</a></div>
        <div class="home_location"><a href="/cities/제주">제주</a></div>`
        const page = document.querySelector(".page_dot");
        page.innerHTML ='<img src="/static/img/page_3.svg" alt="">'
      }
    }
  }
};

// mainList.html 부분
const requestGo = new XMLHttpRequest();
const onClickGo = () => {
  requestGo.open("POST", "/listGo/", true);
  requestGo.setRequestHeader(
    "Content-Type",
    "application/x-www-form-urlencoded"
  );
  var location, category, detail;
  const locList = document.getElementsByName("location"); //장소
  locList.forEach((loc) => {
    if (loc.checked) {
      location = loc.value;
    }
  });

  const cateSelected = document.querySelector(".selected-category").innerHTML; //카테고리
  if (cateSelected.includes("카페")) {
    category = "cafe";
  } else if (cateSelected.includes("숙소")) {
    category = "accomodation";
  } else if (cateSelected.includes("장소")) {
    category = "place";
  }
  const detailList = document.getElementsByName("detail"); //세부 옵션
  detailList.forEach((d) => {
    if (d.checked) {
      detail = d.value;
    }
  });
  requestGo.send(
    JSON.stringify({ location: location, category: category, detail: detail })
  );
};

requestGo.onreadystatechange = () => {
  if (requestGo.readyState === XMLHttpRequest.DONE) {
    if (requestGo.status < 400) {
      test = document.querySelector(".right");
      test.innerHTML = "";
      const { list } = JSON.parse(requestGo.response);
      console.log(list);
      for (var i = 0; i < list.length; i++) {
        const add = document.createElement("div");
        add.classList.add("list-box");
        add.innerHTML = `${list[i]["name"]} ${list[i]["address"]} ${list[i]["phone"]}`;
        test.append(add);
      }
    }
  }
};
// const { list } = JSON.parse(requestGo.response);
//       test = document.querySelector(".right");

//       test.appned('p')
//       list.forEach((place) => {
//         const add = document.createElement('p');
//         test.append(add)
//       });
//
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
      const detailBox = document.querySelector(".option-box");
      const locName = document.querySelector(".selected-category");
      locName.innerHTML = `${cate} 세부옵션`;

      if (cate == "카페") {
        detailBox.innerHTML = `<div class="option-col">
    <label>
      <input type="radio" name="detail" value="애견전용" />애견전용
    </label>
    <label>
      <input type="radio" name="detail" value="애견동반" />애견동반
    </label>
  </div>`;
      } else if (cate == "숙소") {
        detailBox.innerHTML = `<div class="option-col">
        <label>
          <input type="radio" name="detail" value="호텔" />호텔
        </label>
        <label>
          <input type="radio" name="detail" value="모텔" />모텔
        </label>
        </div>
        <div class="option-col">
        <label>
          <input type="radio" name="detail" value="리조트" />리조트
        </label>
        <label>
          <input type="radio" name="detail" value="펜션" />펜션
        </label>
      </div>`;
      } else if (cate == "장소") {
        detailBox.innerHTML = `<div class="option-col">
    <label>
      <input type="radio" name="detail" value="공원" />공원
    </label>
    <label>
      <input type="radio" name="detail" value="수영장" />수영장
    </label>  
  </div>
  <label>
    <input type="radio" name="detail" value="해변" />해변
  </label>`;
      }
    }
  }
};

//찜하기 기능
const requestLike = new XMLHttpRequest();
const onClickLike = (id) => {
  const url = "/like/";
  requestLike.open("POST", url, true);
  requestLike.setRequestHeader(
    "content-Type",
    "application/x-www-form-urlencoded"
  );
  requestLike.send(JSON.stringify({ id: id }));
};

requestLike.onreadystatechange = () => {
  if (requestLike.readyState === XMLHttpRequest.DONE) {
    //서버가 응답할 준비를 마침
    const { id, type } = JSON.parse(requestLike.response);
    const element = document.querySelector(`#favorite-${id}`);
    const i = element.querySelector(".like button i");
    i.classList.toggle("fas");
    i.classList.toggle("far");
  }
};
