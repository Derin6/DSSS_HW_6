{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "97e0985d",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "positional argument follows keyword argument (128873087.py, line 10)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Input \u001b[1;32mIn [6]\u001b[1;36m\u001b[0m\n\u001b[1;33m    install_requires[\"numpy\",\"turtles\"],\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m positional argument follows keyword argument\n"
     ]
    }
   ],
   "source": [
    "from distutils.core import setup\n",
    "from setuptools import find_packages\n",
    "\n",
    "setup (\n",
    "    name=\"snowflake\",\n",
    "    version=\"0.1\",\n",
    "    author=\"DSSS\",\n",
    "    author_email=\"derin.cakiroglu@fau.de\",\n",
    "    packages=find_packages(),\n",
    "    install_requires=[\"numpy\",\"turtles\"],\n",
    "\n",
    "\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c0878072",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
