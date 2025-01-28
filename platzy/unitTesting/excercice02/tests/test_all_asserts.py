import unittest

class AllAsertsTests(unittest.TestCase):
    
    def test_assert_equal(self):
        self.assertEqual(10,10)
        self.assertEqual("hola","hola")
        
    def test_assert_True_or_False(self):
        self.assertTrue("es" == "es") # True
        self.assertFalse("es" != "es") # False
        
    def test_asser_raises(self):
        with self.assertRaises(ValueError):
            int("noSoyUnNumero")
            
    def test_assert_in(self):
        self.assertIn(10, [2,4,5,10])
        self.assertNotIn(1, [2,4,5,10])
        
    def test_assert_diccionario(self):
        userReference = {"firstName": "Rigo", "lastName":"Rios"}
        userReferenceSet = {"firstName", "Rigo", "lastName","Rios"}
        self.assertDictEqual(
            {"firstName": "Rigo", "lastName":"Rios"},
            userReference
        )
        self.assertSetEqual(
            {"firstName",  "Rigo", "lastName", "Rios"},
            userReferenceSet
        )
        
    @unittest.skip("Desarrollo en progreso")
    def test_skip_test(self):
        self.assertTrue("hola" == "adios") # True
        
    variToTestFollowTest = "SERVER_A"
    
    @unittest.skipIf(variToTestFollowTest == "SERVER_A", f"Se salta por q estamos en el servidor {variToTestFollowTest} de pruebas a")
    def test_skip_if(self):
        self.assertTrue("hola" == "adios") # True
        
    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertEqual(100, 10)