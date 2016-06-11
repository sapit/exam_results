function get_panel(title,content){
	console.log(title);
	console.log(content)
	panel_class="panel-danger"
	if(content.trim()=="NO RESULT")
		panel_class="panel-warning"
	panel=	"<div class='panel " + panel_class + "'style='margin-top:10px;margin-bot:10px;'>"+
			  "<div class='panel-heading'>"+
			    "<h3 class='panel-title'>" + title + "</h3>"+
			  "</div>"+
			  "<div class='panel-body'>"+
			    "" + content + ""+
			  "</div>"+
			"</div>"
	return panel

}

$(document).ready(function(){
	$("#Go").on('click', function(){
		var userr = $("#username").val();
		var passw = $("#password").val();
		console.log(userr);
		console.log(passw);
		$.ajax({
	        url : '/results', // the endpoint,commonly same url
	        type : "POST", // http method
	        data : {user:userr,
	                pass:passw
	            }, // data sent with the post request

	        // handle a successful response
	        success : function(data) {
	            console.log(data);
	            for(var i in data)
	            	$("#res").append(get_panel(data[i]["code"]+" " +data[i]["name"],data[i]["result"]))
	        		// $('#res').append("<p>"+data[i]["code"]+"</p>"+
	        		// 	"<p>"+data[i]["name"]+"</p>"+
	        		// 	"<p>"+data[i]["result"]+"</p>");    

	        	// panel_class="panel-default"
		        

	        },
	        
	        // handle a non-successful response
	        error : function(xhr,errmsg,err) {
	            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
	        }
	    });	
	})
	

})