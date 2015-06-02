Scarlett.PlacesView = Backbone.View.extend({
    template: _.template($('#places-tmpl').html()),
    events: {
        'click #add': 'clickAdd',
        'enter #add': 'clickAdd',
        'keyup .placeInput': 'enterPlace',
        'click a.delete': 'clickDelete'
    },

    initialize: function() {
        this.collection = Scarlett.places;
    },

    render: function() {
        this.$el.html(this.template({
            collection: this.collection
        }));
        return this;
    },

    clickAdd: function(e) {
        e.preventDefault();
        if($("#name").val()) {
            this.collection.addItem({
                name: $("#name").val()
            });
        }
    },

    enterPlace: function(e) {
        if(e.keyCode == 13) { // enter key
            this.saveModel(e);
        }
    },

    // for update
    saveModel: function(e){
        var id = $(e.target).parent().find("a").attr("data-id");
        var model = this.collection.findWhere({id:parseInt(id)});
        var me = this;
        return model.save({
            name: $(e.target).val()
        }, {
            wait:true,
            success: function() { me.render(); }
        });
    },

    clickDelete: function(e) {
        e.preventDefault();
        var id = $(e.target).closest("a").attr("data-id");
        var model = this.collection.findWhere({id:parseInt(id)});
        var me = this;
        model.destroy({
            wait: true,
            success: function() { me.render(); },
            error: function() { console.log("ehh error while deleting"); }
        });
    }
});
