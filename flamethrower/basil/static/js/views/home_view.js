Scarlett.HomeView = Backbone.View.extend({
    template: _.template($('#transactions-tmpl').html()),
    events: {
    },

    initialize: function() {
        console.log("HomeView initialize");
    },

    // TODO - refactor this
    render: function() {
        this.$el.html(this.template());
        return this;
    }
});
