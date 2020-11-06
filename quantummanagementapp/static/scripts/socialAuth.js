const useAppState = () => {
  let appState = [];
  return [() => appState.slice(), (newAppState) => (appState = newAppState.splice(0))];
};

// function statusChangeCallback(response) {
//   // Called with the results from FB.getLoginStatus().
//   console.log("statusChangeCallback");
//   console.log(response); // The current login status of the person.
//   if (response.status === "connected") {
//     // Logged into your webpage and Facebook.
//     testAPI();
//   } else {
//     // Not logged into your webpage or we are unable to tell.
//     // document.getElementById("status").innerHTML = "Please log " + "into this webpage.";
//   }
// }

// function checkLoginState() {
//   // Called when a person is finished with the Login Button.
//   FB.getLoginStatus(function (response) {
//     // See the onlogin handler
//     statusChangeCallback(response);
//   });
// }





// (function(d, s, id){
//     var js, fjs = d.getElementsByTagName(s)[0];
//     if (d.getElementById(id)) {return;}
//     js = d.createElement(s); js.id = id;
//     js.src = "https://connect.facebook.net/en_US/sdk.js";
//     fjs.parentNode.insertBefore(js, fjs);
//  }(document, 'script', 'facebook-jssdk'));

// window.fbAsyncInit = function () {
//   FB.init({
//     appId: "373817170537484",
//     cookie: true, // Enable cookies to allow the server to access the session.
//     xfbml: true, // Parse social plugins on this webpage.
//     version: "v8.0", // Use this Graph API version for this call.
//   });

//   FB.getLoginStatus(function (response) {
//     // Called after the JS SDK has been initialized.
//     statusChangeCallback(response); // Returns the login status.
//   });

// };

// function testAPI() {
//   // Testing Graph API after login.  See statusChangeCallback() for when this call is made.
//   console.log("Welcome!  Fetching your information.... ");
//   FB.api("/me", function (response) {
//     console.log("Successful login for: " + response.name);
//     document.getElementById("status").innerHTML = "Thanks for logging in, " + response.name + "!";
//   });
    
//   FB.login(function(response) {
//     if (response.authResponse) {
//      console.log('Welcome!  Fetching your information.... ');
//      FB.api('/me', function(response) {
//        console.log('Good to see you, ' + response.name + '.');
//      });
//     } else {
//      console.log('User cancelled login or did not fully authorize.');
//     }
// });
// }



// const getFacebookCreds = async (id) => {
//     const origin = window.location.origin;
//     try {
//       const response = await fetch(`${origin}/usersocialauth/${1}`, {
//         method: "GET",
//         headers: {
//           "Content-Type": "application/json",
//           Accept: "application/json",
//         },
//       });
//       if (response.ok) {
//         return await response.json();
//       }
//       throw new Error("Request Failed");
//     } catch (err) {
//       console.log(err);
//     }
//   };

// const fetchFacebookSocial = async (userId) => {
//     const user = await getFacebookCreds(userId);
//     console.log(user)
// }

// fetchFacebookSocial(1);

// function checkLoginState() {
// const [appState, setAppState] = useAppState();
// FB.getLoginStatus(function (response) {
// setAppState([response])
// const res = appState();
// const state = JSON.parse(res)
// sessionStorage.setItem("appState", state)
// state.push(status)
// statusChangeCallback(response);
//     });
// };

// function loginfb() {
//     FB.login(function (response) {
//         if (response.authResponse) {
//             console.log('Welcome!  Fetching your information.... ');
//             FB.api('/me', function (response) {
//                 checkLoginState()
//             });
//         } else {
//             console.log('User cancelled login or did not fully authorize.');
//         }
//     }, { scope: 'public_profile,read_insights,pages_show_list,instagram_basic,pages_read_engagement' });
// }

// FB.login(function(response) {
//     if (response.status === 'connected') {
//       // Logged into your webpage and Facebook.
//     } else {
//       // The person is not logged into your webpage or we are unable to tell.
//     }
// });

// FB.logout(function(response) {
//     // Person is now logged out
//  });
// function statusChangeCallback(response) {
//     console.log({response})
// if (response.status == 'connected') {
//     var xhr = new XMLHttpRequest();
//     xhr.open('POST', window.location.origin + '/facebook');
//     xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

//     msg = 'access_token' + '=' + response.authResponse.accessToken + '&' + 'user_id' + '=' + response.authResponse.userID

//     xhr.onload = function () {
//         confetti.start(2000)
//         setTimeout(getSocial, 3000)
//         getKeysLoginsTags()
//     };
//     xhr.send(msg);
//     const origin = window.location.origin;
//     console.log("ORIGN", origin)
//     window.location.href = origin + "/login/home"

// }
// }
