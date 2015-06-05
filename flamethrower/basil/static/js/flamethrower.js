window.Scarlett = {};

Scarlett.Router = Backbone.Router.extend({
    routes: {
        ':places(/)': 'visitPlaces',
        '': 'visitHome'
    },

    initialize: function(places) {
        Scarlett.places = places;
    },

    visitHome: function() {
        this.homeView = new Scarlett.HomeView();
        this.setCurrentView(this.homeView);
    },

    visitPlaces: function() {
        this.placesView = new Scarlett.PlacesView();
        this.setCurrentView(this.placesView);
    },

    setCurrentView: function(view) {
        var $content = $("#container");
        $content.empty();
        $content.html(view.render().el);
    }
});


Scarlett.initializeAjax = function(csrfToken) {
    function csrfSafeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    function sameOrigin(url) {
        var host = document.location.host;
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                xhr.setRequestHeader("X-CSRFToken", csrfToken);
            }
        }
    });
}
