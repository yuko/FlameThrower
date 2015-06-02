Scarlett.PlaceCollection = Backbone.Collection.extend({
    model: Scarlett.PlaceModel,
    url: "/basil/places/",

    addItem: function(init_attrs) {
        var attrs = _.isEmpty(init_attrs) ? {} : init_attrs;
        var newModel = this.create(attrs, {
            wait: true,
            success: this.refreshView,
            error: this.showAddError
        });
        this.listenToOnce(newModel, 'sync', function(){
            // why is newModel.get("id") undefined??
            this.trigger('createNew', newModel.get('name'));
        });

        /* works for adding on client side
        var newModel = new Scarlett.PlaceModel({name: 'oh hai'});
        this.add(newModel);
        */
    },

    refreshView: function() {
        // ehh ugly, make this clean!
        window.app.placesView.render();
    },

    showAddError: function(e){
        console.log("ehhh, showAddError...", e);
    }
});
