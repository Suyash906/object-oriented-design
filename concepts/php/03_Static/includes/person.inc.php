<?php

class Person {
    private $name;
    private $eyeColor;
    private $age;

    public static $drinkingAge = 21;

    public function  __construct($name, $eyeColor, $age)
    {
        $this->name = $name;
        $this->eyeColor = $eyeColor;
        $this->age = $age;
    }

    /**
     * @return mixed
     */
    public function getName()
    {
        return $this->name;
    }

    /**
     * @param mixed $name
     */
    public function setName($name)
    {
        $this->name = $name;
    }

    /**
     * @return mixed
     */
    public function getEyeColor()
    {
        return $this->eyeColor;
    }

    /**
     * @param mixed $eyeColor
     */
    public function setEyeColor($eyeColor)
    {
        $this->eyeColor = $eyeColor;
    }

    /**
     * @return mixed
     */
    public function getAge()
    {
        return $this->age;
    }

    /**
     * @param mixed $age
     */
    public function setAge($age)
    {
        $this->age = $age;
    }

    /**
     * @param int $drinkingAge
     */
    public static function setDrinkingAge($drinkingAge)
    {
        self::$drinkingAge = $drinkingAge;
    }

    /**
     * @return int
     */
    public static function getDrinkingAge()
    {
        return self::$drinkingAge;
    }
}
