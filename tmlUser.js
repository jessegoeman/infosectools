import TMLUser from '@tomorrowland/sso'

const tmlUser = new TMLUser();
tmlUser.getUser()
    .then(user => {
        // User is logged in, store this for reuse
        // Access properties like givenName:
        alert(user.givenName + ' is logged in');
    })
    .catch(error => {
        // Something went wrong, user is probably not correctly authenticated
        // Redirect to login with callback to get back here
        window.location = 'https://my.tomorrowland.com/login?callback=' + window.location;
    });