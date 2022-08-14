const requestMainListLeft = new XMLHttpRequest();
const onClickMainListLeft = () => {
  requestMainListLeft.open("POST", "/btn_left/", true);
  requestMainListLeft.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
  requestMainListLeft.send(JSON.stringify({}));
};

requestMainListLeft.onreadystatechange = () => {
  if (requestMainListLeft.readyState === XMLHttpRequest.DONE) {
    if (requestMainListLeft.status <= 400) {
      let element = document.querySelector("#page-num"); 
      let count = Number(element.innerHTML) - 1; 
      
      if (count == -1) {
        count = 0
      }

      element.innerHTML = `${count}`;
      
      const locationSet = document.querySelector(".shift-locations");
      locationSet.innerHTML =`{% for place in list%}
          {% if ${count*5+1} <= forloop.counter <= ${(count+1)*5} %} 
              <div class="list-box-right">
                <div class="img-box"><img src="" alt="" /></div>
                <div class="accom-text-box">
                  <h1>
                    <a href="/{{category}}/{{place.id}}" class="name">{{place.name}}</a>
                  </h1>
                  <span class="type">{{place.type}}</span>
                  <h3 class="phone">{{place.phone}}</h3>
                  <div class="favorite" id="favorite-{{favorite.id}}">
                    <div class="like">
                      <button type="submit" onclick="onClickLike({{ favorite.id }} )">
                        {% csrf_token %} {% if favorite.like %}
                        <i class="fas fa-heart"></i>
                        {%else%}
                        <i class="far fa-heart"></i>
                        {%endif%}
                      </button>
                    </div>
                  </div>
                </div>
              </div>
          {% endif %}
      {% endfor %}`
    }
  }
};