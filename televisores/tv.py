class TV:
    _numTV = 0

    _marca = ""
    _canal = 1
    _precio = 500
    _estado = False
    _volumen = 1
    _control = None

    def __init__(self, marca, estado):
        self._marca = marca
        self._estado = estado
        TV._numTV += 1

    # Setters y Getters para los atributos de la clase TV
    def getMarca(self):
        return self._marca
    def setMarca(self, marca):
        self._marca = marca

    def getCanal(self):
        return self._canal
    def setCanal(self, canal):
        if (self._estado and 1 <= canal <= 120):
            self._canal = canal

    def getPrecio(self):
        return self._precio
    def setPrecio(self, precio):
        self._precio = precio

    def getVolumen(self):
        return self._volumen
    def setVolumen(self, volumen):
        if (self._estado and 0 <= volumen <= 7):
            self._volumen = volumen

    def getControl(self):
        return self._control
    def setControl(self, control):
        self._control = control

    def getNumTV():
        return TV._numTV
    def setNumTV(numTV):
        TV._numTV = numTV

    def getEstado(self):
        return self._estado

    # Alternadores de estado de TV
    def turnOn(self):
        self._estado = True
    def turnOff(self):
        self._estado = False

    # Cambio de canal
    def canalUp(self):
        if (self._estado and self._canal < 120):
            self._canal += 1

    def canalDown(self):
        if (self._estado and self._canal > 1):
            self._canal -= 1

    # Aumento y disminución de volumen
    def volumenUp(self):
        if (self._estado and self._volumen < 7):
            self._volumen += 1
    def volumenDown (self):
        if (self._estado and self._volumen > 0):
            self._volumen -= 1