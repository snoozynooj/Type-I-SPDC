# Type-II-SPDC
Different Script are for differents type of crystals and wevalenghts
## **Type-II_uniaxial** 
This file use a sellmeier equation given by
$n^{2}(\lambda) = A + \frac{B_1\lambda^{2}}{\lambda^{2}-C_1} + \frac{B_2\lambda^{2}}{\lambda^{2}-C_2}$
to calculate the value of the optical axis angle that ensure a collinear non-degenerative SPDC, then using the $\chi^{(2)}$ the algorithm calculate the azimuthal angle $\phi$ that maximize the $d_{eff}$, then using this $d_{eff}$ and the properties of the crystal the algorithm calculate the Photon counting rate per second, per millimeter length of crystal, per milliwatt of potency pumped.

As an output we get the following images:

$d_{eff}$ v/s azimuthal angle

<img src="MOFTIL_deff.png" width="400">


$G^{(2)}$ as a function of the characteristic time

<img src="MOFTIL_G2.png" width="400">
