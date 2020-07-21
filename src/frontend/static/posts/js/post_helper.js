var all_category_list= "http://www.googlespot.org/api/v1/post/categories/";
var default_category = "all";
var global_tracking_category ="all";
var global_category_default_endpoint = "http://www.googlespot.org/api/v1/post/all/"
var global_category_endpoint = "http://www.googlespot.org/api/v1/post/categories/"
var next_endpoint = null;

function ajax_request_card(api){
        $.ajax({
          url: api,
          type: "GET",
          success: function (result) {
            next_endpoint =result.next;
            if(result.results.length > 0){
              result.results.forEach(function(post){
                title = post.title;
                title_description = post.title_description;
                post_thumbnail = post.post_thumbnail;
                frontend_slug_url = post.frontend_slug_url;
                // if(post_thumbnail === null){
                //   post_thumbnail='https://materializecss.com/images/office.jpg';
                // }
                var singleCard = '<div class="col s12 m6 l6 xl4">';
                  singleCard += `               
                    <div class="card medium hoverable">
                      
                      <div class="card-image waves-effect waves-block waves-light">
                        
                        <img
                          src="`+post_thumbnail+`"
                          alt="thumbnail"
                        />
                        <span class="card-title">`+global_tracking_category+`</span>
                      </div>
                      <div class="card-content">
                        <span class="grey-text text-darken-4"
                          >`+title+`</span
                        >
                      </div>
                      <div class="card-action">
                          <a class="btn deep-purple accent-4 z-depth-0" href="${frontend_slug_url}">Read more</a>
                      </div>
                      
                    </div>`;

                    singleCard += " </div>";
                $('#main_layout').append(singleCard);

              });
             
            }
        
          },
          error: function (error) {
            console.log(error);
          },
        });

      }





