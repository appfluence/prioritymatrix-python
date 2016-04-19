import json
import demjson


class Icon(object):
    """
    This is the icon class.

    """

    icon_name = "blank.png"

    def __init__(self, icon_name = "blank.png"):
        """
        Constructor of Icon class:

        :param icon_name: The name of the icon
        :type icon_name: string

        .. note:: The name of the icon by default is "blank.png"
        .. note:: The name of the icon must be one of the next list: "blackcircletransparent128.png", "blank.png", "blue_airplane128.png", "blue_bicyclist128.png", "blue_book128.png", "blue_businessbox128.png", "blue_businessdoc128.png", "blue_businessdoc2128.png", "blue_cabinet128.png", "blue_car128.png", "blue_clock128.png", "blue_cocktail128.png", "blue_coffee128.png", "blue_creditcard128.png", "blue_diamond128.png", "blue_dining128.png", "blue_document128.png", "blue_envelope128.png", "blue_euro128.png", "blue_fruit128.png", "blue_gift128.png", "blue_heart128.png", "blue_home128.png", "blue_hospital128.png", "blue_key128.png", "blue_lightbulb128.png", "blue_paperclip128.png", "blue_pencil128.png", "blue_pound128.png", "blue_printer128.png", "blue_santaclaus128.png", "blue_scale128.png", "blue_ship128.png", "blue_shovel128.png", "blue_stop128.png", "blue_telephone128.png", "blue_thumbsdown128.png", "blue_thumbsup128.png", "blue_world128.png", "blue_wrench128.png", "coffee128.png", "default_icon.png", "empty_orange128.png", "green_cellphone128.png", "green_checkmark128.png", "green_circle128.png", "green_envelope128.png", "green_exclamation128.png", "green_filecabinet128.png", "green_house128.png", "green_laptop128.png", "green_pen128.png", "green_questionmark128.png", "green_smiley128.png", "green_text128.png", "green_world128.png", "news128.png", "orange_00128.png", "orange_01128.png", "orange_02128.png", "orange_03128.png", "orange_04128.png", "orange_05128.png", "orange_06128.png", "orange_07128.png", "orange_08128.png", "orange_09128.png", "orange_10128.png", "orange_baby128.png", "orange_brain128.png", "orange_briefcase128.png", "orange_bubble128.png", "orange_camera128.png", "orange_diamond128.png", "orange_family128.png", "orange_fire128.png", "orange_girl128.png", "orange_headphones128.png", "orange_information128.png", "orange_island128.png", "orange_male128.png", "orange_percentage128.png", "orange_pill128.png", "orange_prescription128.png", "orange_star128.png", "orange_stroller128.png", "orange_studying128.png", "orange_tree128.png", "plainbluecircle128.png", "plaingraycircle128.png", "plaingreencircle128.png", "plainmagentacircle128.png", "plainpurplecircle128.png", "plainredcircle128.png", "plainwhitecircle128.png", "plainyellowcircle128.png", "red_0128.png", "red_10128.png", "red_1128.png", "red_2128.png", "red_3128.png", "red_4128.png", "red_5128.png", "red_6128.png", "red_7128.png", "red_8128.png", "red_9128.png", "red_asterisk128.png", "red_clock128.png", "red_dollar128.png", "red_dot.png", "red_exclamation128.png", "red_fire128.png", "red_graph128.png", "red_greater128.png", "red_idea128.png", "red_ipod128.png", "red_musicnote128.png", "red_piano128.png", "red_shoppingcart128.png", "red_smaller128.png", "red_tools128.png", "red_x128.png", "star128.png" or "star_full128.png".

        """
        possible_names = ["blackcircletransparent128.png", "blank.png", "blue_airplane128.png", "blue_bicyclist128.png", "blue_book128.png", "blue_businessbox128.png", "blue_businessdoc128.png", "blue_businessdoc2128.png", "blue_cabinet128.png", "blue_car128.png", "blue_clock128.png", "blue_cocktail128.png", "blue_coffee128.png", "blue_creditcard128.png", "blue_diamond128.png", "blue_dining128.png", "blue_document128.png", "blue_envelope128.png", "blue_euro128.png", "blue_fruit128.png", "blue_gift128.png", "blue_heart128.png", "blue_home128.png", "blue_hospital128.png", "blue_key128.png", "blue_lightbulb128.png", "blue_paperclip128.png", "blue_pencil128.png", "blue_pound128.png", "blue_printer128.png", "blue_santaclaus128.png", "blue_scale128.png", "blue_ship128.png", "blue_shovel128.png", "blue_stop128.png", "blue_telephone128.png", "blue_thumbsdown128.png", "blue_thumbsup128.png", "blue_world128.png", "blue_wrench128.png", "coffee128.png", "default_icon.png", "empty_orange128.png", "green_cellphone128.png", "green_checkmark128.png", "green_circle128.png", "green_envelope128.png", "green_exclamation128.png", "green_filecabinet128.png", "green_house128.png", "green_laptop128.png", "green_pen128.png", "green_questionmark128.png", "green_smiley128.png", "green_text128.png", "green_world128.png", "news128.png", "orange_00128.png", "orange_01128.png", "orange_02128.png", "orange_03128.png", "orange_04128.png", "orange_05128.png", "orange_06128.png", "orange_07128.png", "orange_08128.png", "orange_09128.png", "orange_10128.png", "orange_baby128.png", "orange_brain128.png", "orange_briefcase128.png", "orange_bubble128.png", "orange_camera128.png", "orange_diamond128.png", "orange_family128.png", "orange_fire128.png", "orange_girl128.png", "orange_headphones128.png", "orange_information128.png", "orange_island128.png", "orange_male128.png", "orange_percentage128.png", "orange_pill128.png", "orange_prescription128.png", "orange_star128.png", "orange_stroller128.png", "orange_studying128.png", "orange_tree128.png", "plainbluecircle128.png", "plaingraycircle128.png", "plaingreencircle128.png", "plainmagentacircle128.png", "plainpurplecircle128.png", "plainredcircle128.png", "plainwhitecircle128.png", "plainyellowcircle128.png", "red_0128.png", "red_10128.png", "red_1128.png", "red_2128.png", "red_3128.png", "red_4128.png", "red_5128.png", "red_6128.png", "red_7128.png", "red_8128.png", "red_9128.png", "red_asterisk128.png", "red_clock128.png", "red_dollar128.png", "red_dot.png", "red_exclamation128.png", "red_fire128.png", "red_graph128.png", "red_greater128.png", "red_idea128.png", "red_ipod128.png", "red_musicnote128.png", "red_piano128.png", "red_shoppingcart128.png", "red_smaller128.png", "red_tools128.png", "red_x128.png", "star128.png", "star_full128.png"]

        if (icon_name in possible_names):
            self.icon_name = icon_name

    def getName(self):
        return icon_name

    def setName(self, icon_name):
        if (icon_name in possible_names):
            self.icon_name = icon_name
