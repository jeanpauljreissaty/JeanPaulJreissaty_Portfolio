/*
* Fichier: roiException.hpp
* Auteur: Leo Rouleau (2452959) et Jean-Paul Jreissaty (2462433)
* Description: Implementation de l'exception pour le cas ou on essaye de creer plus de 2 rois dans un jeu d'echec.
*/

#pragma once

#include <stdexcept>
#include <string>

namespace logique {

	class RoiException : public std::runtime_error {
	public:
		explicit RoiException(const std::string& message)
			: std::runtime_error(message) {}
	};

}
