import unittest
from Televison import Television

class TelevisionTest (unittest.TestCase):
    def setUp(self):
       self.tv = Television()

    def test_that_I_Plug_TV_It_is_Initially_Off(self):

        self.assertEqual(self.tv.check_tv_power_status(),False)
    # def test_That_TV_Can_be_Turned_Off_After_Use(self):
    #     self.assertFalse(self.tv.is_on())

    #     self.tv.turn_on()
    #     self.tv.turn_off()
    #     self.assertFalse(self.tv.is_on())

    

    def test_That_I_Turn_TV_On_I_Can_Increase_Volume(self):
        self.assertFalse(self.tv.check_tv_power_status())
        self.tv.turn_on()
        volume = self.tv.get_volume()
        self.assertEqual(volume,0)
        self.tv.increase_volume()
        volume = self.tv.get_volume()
        self.assertEqual(volume, 1)

    def test_That_I_Try_To_Increase_Volume_Without_Turning_TV_On_Volume_Remains_Same_And_Throws_An_Error(self):
        self.assertFalse(self.tv.check_tv_power_status())
        initial_volume = self.tv.get_volume()
        with self.assertRaises(ValueError):self.tv.increase_volume()
        self.assertEqual(0, initial_volume)

    def test_That_I_Try_To_Decrease_Volume_Without_Turning_TV_On_Volume_Remains_Same_And_Throws_An_Error(self):
        self.assertFalse(self.tv.check_tv_power_status())
        initial_volume = self.tv.get_volume()
        with self.assertRaises(ValueError):self.tv.decrease_volume()
        self.assertEqual(0, initial_volume)

    def test_That_I_Turn_On_TV_I_Can_Not_Increase_Past_MAx(self):
        self.tv.turn_on()
        initial_volume = self.tv.get_volume()
        self.assertEqual(0, initial_volume)

        for volume in range(150):
            self.tv.increase_volume()
        self.assertEqual(self.tv.get_volume(), self.tv.MAX_VOLUME)

    def test_That_I_Turn_On_TV_I_Can_Not_Reduce_Past_Min(self):
        self.tv.turn_on()
        initial_volume = self.tv.get_volume()
        self.assertEqual(0, initial_volume)

        for volume in range(100):
            self.tv.decrease_volume()
        self.assertEqual(self.tv.get_volume(), self.tv.MIN_VOLUME)

    def test_That_I_Turn_TV_On_I_Can_Set_Channel(self):
        self.tv.turn_on()
        initial_channel = self.tv.get_channel()
        self.assertEqual(1,initial_channel)

        self.tv.set_channel(20)
        self.assertEqual(20,self.tv.get_channel())

    def test_That_I_Turn_On_TV_I_Try_To_Set_Channel_Above_The_Last_Channel_It_Throws_An_Error(self):
        self.tv.turn_on()
        initial_channel = self.tv.get_channel()
        self.assertEqual(1,initial_channel)

        with self.assertRaises(ValueError):self.tv.set_channel(101)
        self.assertEqual(1,initial_channel)


    def test_That_I_Turn_On_TV_I_Try_To_Set_Channel_Below_The_First_Channel_It_Throws_An_Error(self):
        self.tv.turn_on()
        initial_channel = self.tv.get_channel()
        self.assertEqual(1, initial_channel)

        with self.assertRaises(ValueError): self.tv.set_channel(0)
        self.assertEqual(1,initial_channel)

    def test_That_I_Try_To_Set_Channel_Without_Turning_TV_On_Throws_An_Error(self):
        initial_channel = self.tv.get_channel()
        self.assertEqual(1,initial_channel)

        with self.assertRaises(ValueError): self.tv.set_channel(25)
        self.assertEqual(1, initial_channel)

    def test_That_I_Turn_On_TV_I_Can_Change_Channel_Forward(self):
        self.tv.turn_on()
        initial_channel = self.tv.get_channel()
        self.assertEqual(1, initial_channel)

        self.tv.next_channel()
        self.assertEqual(2,self.tv.get_channel())

    def test_That_I_Turn_On_TV_I_Can_Change_Channel_Backward(self):
        self.tv.turn_on()
        initial_channel = self.tv.get_channel()
        self.assertEqual(1, initial_channel)

        self.tv.next_channel()
        self.tv.previous_channel()
        self.assertEqual(1, self.tv.get_channel())

    def test_That_I_Turn_On_TV_And_I_Change_Channel_Past_The_Last_Channel_It_Starts_From_The_First(self):
        self.tv.turn_on()
        initial_channel = self.tv.get_channel()
        self.assertEqual(1, initial_channel)

        self.tv.set_channel(100)
        self.tv.next_channel()
        self.assertEqual(1,self.tv.get_channel())

    def test_That_I_Turn_On_TV_And_I_Change_Channel_Back_From_The_First_Channel_It_Goes_The_Last(self):
        self.tv.turn_on()
        initial_channel = self.tv.get_channel()
        self.assertEqual(1, initial_channel)

        self.tv.previous_channel()
        self.assertEqual(100, self.tv.get_channel())






if __name__ == '__main__':
    unittest.main()
