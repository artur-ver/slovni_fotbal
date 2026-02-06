#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import random
import unicodedata
from pathlib import Path
from typing import Dict, Tuple, List

# ----------------------------

# Helper functions

# ----------------------------

def normalize_word(word: str) -> str:
   
    """
    
    Normalizace a word:
    
    - lowercase
    - remove diacritics
    - keep letters only
    
    """
    # Převod na malá písmena a odstranění bílých znaků
    
    word = word.strip().lower()
    word = unicodedata.normalize('NFKD', word)
    word = ''.join(ch for ch in word if not unicodedata.combining(ch))
    return ''.join(ch for ch in word if ch.isalpha())


def first_char(word: str) -> str:
    """Return the first char, treating 'ch' as one letter."""
    # V češtině je 'ch' jedním znakem
    return 'ch' if word.startswith('ch') else (word[0] if word else '')


def last_char(word: str) -> str:
    """Return the last char, treating 'ch' as one letter."""
    # V češtině je 'ch' jedním znakem - kontrolujeme na konci slova
    return 'ch' if word.endswith('ch') else (word[-1] if word else '')

# ----------------------------
# Load words
# ----------------------------


def load_words(folder: str = "vstupy") -> Dict[str, str]:
    """
    Load all words from .txt and .json files under 'vstupy',
    Returns a dict. {normalized_word: original_word}.
    
    """
    # Načtení slov z textových a JSON souborů pro hru
    folder_path = Path(folder)
    words_map: Dict[str, str] = {}

    if not folder_path.exists():
        folder_path.mkdir()
        return words_map

    for file in folder_path.rglob("*"):
        
        if not file.is_file():
            continue
        try:
            data: List[str] = []
            
            if file.suffix == ".txt":
                
                data = [line.strip() for line in file.read_text(encoding="utf-8").splitlines() if line.strip()]
            elif file.suffix == ".json":
                
                raw = json.loads(file.read_text(encoding="utf-8"))
                
                if isinstance(raw, list):
                    data = raw
                    
                elif isinstance(raw, dict):
                    for v in raw.values():
                        
                        if isinstance(v, list):
                            data.extend(v)
            for w in data:
                norm = normalize_word(str(w))
                
                if norm and norm not in words_map:
                    words_map[norm] = str(w)
        except Exception as e:
            print(f"[WARN] Could not read {file}: {e}")
            
            continue
    return words_map

# ----------------------------
# Game logic
# ----------------------------


class SlovniFotbal:
    """Class for slovní fotbal game. """


    def __init__(self, words_map: Dict[str, str]):
        self.words_map = words_map
        self.used_words: set[str] = set()
        self.required_char: str = ""  		# next letter to play


    def computer_turn(self) -> Tuple[str, str]:
        """Computer chooses a word starting with required_char."""
        # Vybere slova, která nebyla použita a začínají na požadovaný znak
        candidates = [w for w in self.words_map.keys()
                      if w not in self.used_words and first_char(w) == self.required_char]
        if not candidates:
            return "", ""
          
        word_norm = random.choice(candidates)
        
        self.used_words.add(word_norm)
        self.required_char = last_char(word_norm)
        return word_norm, self.words_map[word_norm]


    def player_turn_valid(self, player_input: str) -> Tuple[bool, str]:
        """Check if player's input is valid and return normalized word."""
        # Ověření zda je zadané slovo validní nebo ne
        norm = normalize_word(player_input)
        
        if not norm:
            return False, "Use letters only!"
        
        if first_char(norm) != self.required_char:
            return False, f"Must start with '{self.required_char.upper()}'"
        
        if norm in self.used_words:
            return False, "Word already used!"
        self.used_words.add(norm)
        self.required_char = last_char(norm)
        return True, norm


    def start_game(self):
        """Main game loop."""
        if not self.words_map:
            print("[ERROR] No words loaded in 'vstupy'.")
            return

        print("----- Slovní fotbal: Eda vs Player -----")
        # Počáteční tah počítače
        norm, orig = random.choice(list(self.words_map.items()))
        self.used_words.add(norm)
        self.required_char = last_char(norm)
        print(f"Eda: {orig.upper()}")

        while True:
            # Tah hráče
            player_input = input(f"\nYour turn. Target is letter:   '{self.required_char.upper()}': ").strip()
            if player_input.lower() in ['quit', 'im a loser']:
                print("Eda wins! Better luck next time.")
                break

            valid, result = self.player_turn_valid(player_input)
            if not valid:
                print(f"Invalid move: {result}")
                continue

            # Tah počítače
            comp_norm, comp_word = self.computer_turn()
            if not comp_word:
                print(f"\nEda: 'I don t know any words starting with {self.required_char.upper()}...'")
                print("CONGRATULATIONS! You beat Eda!")
                break
            print(f"Eda: {comp_word.upper()}")


# ----------------------------
# Entry point
# ----------------------------


def main():
    words_map = load_words("vstupy")
    game = SlovniFotbal(words_map)
    game.start_game()

if __name__ == "__main__":
    main()
